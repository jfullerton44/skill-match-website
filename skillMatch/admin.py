from django.contrib import admin


from .models import Student, Class, Skill

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','sex','bio', 'user']


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['prefix',"course_number",'professor','semester']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']



