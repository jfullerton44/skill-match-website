from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Student, Skill, Class



class IndexView(generic.ListView):
    template_name = 'skillMatch/index.html'
    model = Student

class ProfileCreateView(generic.CreateView):
    model = Student
    fields = ('name', 'sex', 'bio')
    success_url = reverse_lazy('skillMatch:index')

def studentProfileView(request, user_id):
    person = get_object_or_404(Student, pk=user_id)
    person_classes = person.classes.all()
    person_skills = person.skills.all()
    return render(request, 'skillMatch/student.html', {'person' : person, 
        'person_classes' : person_classes,
        'person_skills' : person_skills,
    })
    
def home(request):
    return render(request, 'home.html')
