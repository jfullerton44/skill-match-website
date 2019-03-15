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


class ProfileCreateView(generic.CreateView):
    model = Student
    fields = ('name', 'sex', 'bio')
    success_url = reverse_lazy('skillMatch:index')


def studentProfileView(request, user_id):
    person = get_object_or_404(User, username=user_id)
    person = person.student
    person_classes = person.classes.all()
    person_skills = person.skills.all()
    picture = person.picture
    context = {'person' : person, 
                'person_classes' : person_classes, 
                'person_skills' : person_skills,
                'picture' : picture}
    return render(request, 'skillMatch/student.html', context)

def home(request):
    students = [student.user.username for student in Student.objects.all() if student.name]
    context = {
        'students' : students
    }
    return render(request, 'home.html', context)


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'skillMatch/student_update_form.html'
    success_url = reverse_lazy('skillMatch:index')

class ClassCreateView(generic.CreateView):
    model = Class
    fields = ('prefix','course_number','professor','semester')
    success_url = reverse_lazy('skillMatch:index')

def studentListView(request):
    student_name = request.GET.get('usr_query', '')
    students = Student.objects.filter(name__icontains=student_name)
    context = {
        'matching_students' : students
    }

    return render(request, 'skillMatch/student_list.html/', context)