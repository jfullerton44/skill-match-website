from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .forms import StudentForm
from .models import Student, Skill, Class


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
        'person' : person, 
        'person_classes' : person_classes, 
        'person_skills' : person_skills,
        'picture' : picture
    }
    return render(request, 'skillMatch/student.html', context)

class StudentUpdateView(generic.UpdateView):
    model = User
    form_class = StudentForm
    template_name = 'skillMatch/student_update_form.html'
    success_url = reverse_lazy('skillMatch:index')
    slug_field = 'username'
    slug_url_kwarg = 'username'

class ClassCreateView(generic.CreateView):
    model = Class
    fields = ('prefix', 'course_number', 'professor', 'semester')
    success_url = reverse_lazy('skillMatch:index')


class SkillCreateView(generic.CreateView):
    model = Skill
    fields = ('name',)
    success_url = reverse_lazy('skillMatch:index')


def studentListView(request):
    student_name = request.GET.get('usr_query', '')
    students = Student.objects.filter(user__username__icontains=student_name)
    context = {
        'matching_students' : students
    }

    return render(request, 'skillMatch/student_list.html/', context)