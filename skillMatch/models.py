from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    name = models.CharField(max_length=100)
    # computing_id = models.CharField(max_length=6, unique= True)
    bio = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    classes = models.ManyToManyField('Class',blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    picture = models.ImageField(default = "media/default-user.jpg", upload_to='images/')

    def __str__(self):
        return "%s (%s)" % (self.name, self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()


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
        return "%s %s Semester: %s" % (self.prefix, self.course_number, self.semester)