from django.urls import path

from . import views

app_name= 'skillMatch'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addfriend/<slug:user_id>/', views.addfriend, name="addfriend"),
    path('createProfile/', views.ProfileCreateView.as_view(), name='profile_create'),
    path('students/<slug:user_id>/', views.studentProfileView, name='profile'),
    path('students/<slug:user>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('createClass/',views.ClassCreateView.as_view(),name='class_create'),
    path('createSkill/',views.SkillCreateView.as_view(),name='skill_create'),
    path('search/', views.studentListView, name='student_list')
]