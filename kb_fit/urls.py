from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.ExerciseList.as_view(), name='library'),
    path('sessions/', views.sessions, name='sessions'),
    path('sessions/<int:pk>/', views.SessionDetail.as_view(), name='session_detail'),
    path('sessions/create/', views.SessionCreate.as_view(), name='sessions_create'),
]