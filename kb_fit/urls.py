from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.ExerciseList.as_view(), name='library'),

]