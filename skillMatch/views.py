from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .forms import StudentForm
from .models import Student, Skill, Class


class IndexView(generic.ListView):
    template_name = 'skillMatch/index.html'
    model = Student


class ProfileCreateView(generic.CreateView):
    model = Student
    fields = ('name','computing_id', 'sex', 'bio')
    success_url = reverse_lazy('skillMatch:index')


def studentProfileView(request, user_id):
    person = get_object_or_404(Student, computing_id=user_id)
    person_classes = person.classes.all()
    person_skills = person.skills.all()
    context = {'person' : person, 
                'person_classes' : person_classes, 
                'person_skills' : person_skills}
    return render(request, 'skillMatch/student.html', context)


def home(request):
    return render(request, 'home.html')


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'skillMatch/student_update_form.html'