from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.ExerciseList.as_view(), name='library'),
    path('sessions/', views.sessions, name='sessions'),
    path('sessions/<int:pk>/', views.SessionDetail.as_view(), name='session_detail'),
    path('sessions/create/', views.session_create, name='sessions_create'),
    path('sessions/<int:pk>/update/', views.SessionUpdate.as_view(), name='session_update'),
    path('sessions/<int:pk>/delete/', views.SessionDelete.as_view(), name='session_delete'),
]