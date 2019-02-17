from django.urls import path

from . import views

app_name= 'skillMatch'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('createProfile/', views.ProfileCreateView.as_view(),name='profile_create')

]