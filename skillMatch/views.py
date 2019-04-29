from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .forms import StudentForm
from .models import Student, Skill, Class, Post, Comment

class Meta:
    ordering = ['-id']

class IndexView(generic.ListView):
    template_name = 'skillMatch/index.html'
    model = Student
    context_object_name = 'students'
    paginate_by = 5


class ProfileCreateView(generic.CreateView):
    model = Student
    fields = ('name', 'sex', 'bio', 'classes', 'skills', 'picture')
    success_url = reverse_lazy('skillMatch:index')


def studentProfileView(request, user_id):
    person = get_object_or_404(User, username=user_id)
    person_classes = person.student.classes.all().order_by('id')
    person_skills = person.student.skills.all().order_by('id')
    person_friends = person.student.friends.all().order_by('id')
    picture = person.student.picture
    context = {
        'person': person,
        'person_classes': person_classes,
        'person_skills': person_skills,
        'person_friends': person_friends,
        'picture': picture
    }
    return render(request, 'skillMatch/student.html', context)

def classDetailView(request, course_pk) :
    course = get_object_or_404(Class, pk=course_pk)
    students = course.student_set.all().order_by('id')
    context = {
        'course' : course,
        'students' : students
    }
    return render(request, 'skillMatch/course_details.html', context)


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'skillMatch/student_update_form.html'
    success_url = reverse_lazy('skillMatch:index')
    slug_field = 'user'
    slug_url_kwarg = 'user'

    def get_object(self, queryset=None):
        return Student.objects.get(user__username=self.request.user)


class ClassCreateView(generic.CreateView):
    model = Class
    fields = ('prefix', 'course_number', 'professor', 'semester')
    success_url = reverse_lazy('skillMatch:class_list')


class SkillCreateView(generic.CreateView):
    model = Skill
    fields = ('name',)
    success_url = reverse_lazy('skillMatch:skill_list')


class PostCreateView(generic.CreateView):
    model = Post
    fields = ('title', 'content', 'course', 'skills')
    success_url = reverse_lazy('skillMatch:post_list', kwargs={'filter':'True'})
    def form_valid(self, form):
        uname = self.kwargs['username']
        mystudent = Student.objects.get(user__username=uname)
        form.instance.author = mystudent
        return super(PostCreateView, self).form_valid(form)
    # def get_success_url(self):
    #     uname = self.kwargs['username']
    #     self.object.author = Student.objects.get(user__username=uname)
    #     return reverse_lazy('skillMatch:index')


class CommentCreateView(generic.CreateView):
    model = Comment
    fields = ('content',)
    success_url = reverse_lazy('skillMatch:post_list', kwargs={'filter':'True'})

    def form_valid(self, form):
        uname = self.kwargs['user']
        mystudent = Student.objects.get(user__username=uname)
        form.instance.author = mystudent

        postID = self.kwargs['post']
        mypost = Post.objects.get(pk=postID)
        form.instance.post = mypost

        return super(CommentCreateView, self).form_valid(form)


def studentListView(request):
    students = set()
    computing_id = request.GET.get('usr_query', '')
    student_name = request.GET.get('usr_query', '')
    class_name = request.GET.get('usr_query', '')

    id_results = Student.objects.filter(user__username__icontains=computing_id)
    first_name_results = Student.objects.filter(user__first_name__icontains=student_name)
    last_name_results = Student.objects.filter(user__last_name__icontains=student_name)

    students.update(id_results)
    students.update(first_name_results)
    students.update(last_name_results)

    classes = set()
    classes.update(Class.objects.filter(prefix__icontains=class_name))
    classes.update(Class.objects.filter(course_number__icontains=class_name))
    classes.update(Class.objects.filter(semester__icontains=class_name))
    classes.update(Class.objects.filter(professor__icontains=class_name))

    skills = set()
    skills.update(Skill.objects.filter(name__icontains=class_name))

    context = {
        'matching_students': students,
        'matching_classes' : classes,
        'matching_skills' : skills
    }

    return render(request, 'skillMatch/student_list.html/', context)



def addfriend(request, student_id):
    friend_being_added = Student.objects.get(user__username=student_id)
    person_adding_friend = Student.objects.get(user__username=request.user)
    person_adding_friend.friends.add(friend_being_added)
    person_adding_friend.save()
    return studentProfileView(request, request.user.username)


def removefriend(request, student_id):
    friend_being_removed = Student.objects.get(user__username=student_id)
    person_removing_friend = Student.objects.get(user__username=request.user)
    person_removing_friend.friends.remove(friend_being_removed)
    person_removing_friend.save()
    return studentProfileView(request, request.user.username)


class skillListView(generic.ListView):
    template_name = 'skillMatch/skill_list.html'
    model = Skill
    context_object_name = 'skills'
    paginate_by = 15


def addSkill(request, user_id, skill_id):
    person = get_object_or_404(User, username=user_id)
    student = person.student
    person_skills = person.student.skills.all().order_by('id')
    skill = Skill.objects.filter(id=skill_id).values_list('id', flat=True)
    student.skills.add(skill[0])
    # student.update()
    return render(request, 'skillMatch/success.html')


class classListView(generic.ListView):
    template_name = 'skillMatch/class_list.html'
    model = Class
    context_object_name = 'classes'
    paginate_by = 15


def addclass(request, user_id, class_id):
    person = get_object_or_404(User, username=user_id)
    student = person.student
    person_class = person.student.classes.all().order_by('id')
    classToAdd = Class.objects.filter(id=class_id).values_list('id', flat=True)
    student.classes.add(classToAdd[0])
    # student.update()
    return render(request, 'skillMatch/success.html')



def postListView(request, filter): # displays every post from newest to oldest, optionally filters for friend posts only
    # add message if filter on but no friends added?
    if filter == "True":  # may only pass in True if user is logged in
        authors = set()
        me = Student.objects.get(user__username=request.user)
        friends = me.friends.all().order_by('id')
        authors.update(friends)
        authors.update({me})
        posts_ordered = Post.objects.filter(author__in=authors).order_by('-date')
    else:
        posts_ordered = Post.objects.all().order_by('-date')


    if posts_ordered:
        post_results = [{'id': post.id, 'author_user': post.author.user.username, 'author_name': post.author.name, 'author_picture': post.author.picture.url,
                         'title': post.title, 'content': post.content, 'course': str(post.course),
                         'skills': [skill.name for skill in post.skills.all()],
                         'comments': [{'author_user': comment.author.user.username, 'author_name': comment.author.name, 'content': comment.content} for comment in Comment.objects.filter(post=post).order_by('date')],
                         'date': post.date}
                        for post in posts_ordered]
        context = {
            'post_results': post_results,
            'filter': filter,
        }
    else:
        context = {}

    return render(request, 'skillMatch/post_list.html/', context)