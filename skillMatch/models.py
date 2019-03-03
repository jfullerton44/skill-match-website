from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    computing_id = models.CharField(max_length=6, unique= True)
    bio = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    classes = models.ManyToManyField('Class',blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.computing_id)


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    prefix = models.CharField(max_length=5)
    course_number = models.CharField(max_length=5)
    professor = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)


    def __str__(self):
        return self.prefix + " "+ self.course_number +" Semester: "+ self.semester