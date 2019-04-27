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
    friends = models.ManyToManyField('Student', blank=True)
    picture = models.ImageField(default = "static/default-user.jpg", upload_to='images/')

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
    semester = models.CharField(max_length=3)

    def __str__(self):
        return "%s %s Semester: %s" % (self.prefix, self.course_number, self.semester)


class Post(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=400)
    course = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)  # up to 1 optional relevant course
    skills = models.ManyToManyField('Skill', blank=True)    # optional relevant skills
    date = models.DateTimeField(auto_now_add=True) # captures time of object creation
    # likes = models.IntegerField()   # upvote and downvote feature?

class Comment(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    # each comment relates to ONE post
    date = models.DateTimeField(auto_now_add=True) # captures time of object creation