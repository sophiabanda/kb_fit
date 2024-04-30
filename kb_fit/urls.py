from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.ExerciseList.as_view(), name='library'),
    path('library/create/', views.ExerciseCreate.as_view(), name='exercise_create'),
    path('library/<int:pk>/', views.ExerciseDetail.as_view(), name='exercise_detail'),
    path('library/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercise_update'),
    path('library/<int:pk>/', views.ExerciseDelete.as_view(), name='exercise_delete'),
    path('sessions/', views.sessions, name='sessions'),
    path('sessions/<int:pk>/', views.SessionDetail.as_view(), name='session_detail'),
    path('sessions/create/', views.session_create, name='sessions_create'),
    path('sessions/<int:pk>/update/', views.SessionUpdate.as_view(), name='session_update'),
    path('sessions/<int:pk>/delete/', views.SessionDelete.as_view(), name='session_delete'),
]