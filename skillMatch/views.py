from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .forms import StudentForm
from .models import Student, Skill, Class, Post


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
    person_classes = person.student.classes.all()
    person_skills = person.student.skills.all()
    picture = person.student.picture
    context = {
        'person': person,
        'person_classes': person_classes,
        'person_skills': person_skills,
        'picture': picture
    }
    return render(request, 'skillMatch/student.html', context)


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
    success_url = reverse_lazy('skillMatch:index')


class SkillCreateView(generic.CreateView):
    model = Skill
    fields = ('name',)
    success_url = reverse_lazy('skillMatch:index')


class PostCreateView(generic.CreateView):
    model = Post
    fields = ('title', 'content', 'course', 'skills')
    success_url = reverse_lazy('skillMatch:index')
    def form_valid(self, form):
        uname = self.kwargs['username']
        mystudent = Student.objects.get(user__username=uname)
        form.instance.author = mystudent
        return super(PostCreateView, self).form_valid(form)
    # def get_success_url(self):
    #     uname = self.kwargs['username']
    #     self.object.author = Student.objects.get(user__username=uname)
    #     return reverse_lazy('skillMatch:index')


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


class skillListView(generic.ListView):
    template_name = 'skillMatch/skill_list.html'
    model = Skill
    context_object_name = 'skills'
    paginate_by = 15


def addSkill(request, user_id, skill_id):
    person = get_object_or_404(User, username=user_id)
    student = person.student
    person_skills = person.student.skills.all()
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
    person_class = person.student.classes.all()
    classToAdd = Class.objects.filter(id=class_id).values_list('id', flat=True)
    student.classes.add(classToAdd[0])
    # student.update()
    return render(request, 'skillMatch/success.html')


    
def postListView(request): # for now, gets every post
    posts_ordered = Post.objects.all().order_by('-date') # descending order
    if posts_ordered:
        post_results = [{'author_user': post.author.user.username, 'author_name': post.author.name, 'author_picture': post.author.picture.url, 'title': post.title, 'content': post.content, 'course': str(post.course), 'skills': [skill.name for skill in post.skills.all()], 'date': post.date}
                        for post in posts_ordered]
        context = {
            'post_results': post_results
        }
    else:
        context = {}

    return render(request, 'skillMatch/post_list.html/', context)