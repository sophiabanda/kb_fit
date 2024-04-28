from django.shortcuts import render
from .models import Exercise, SessionEntry

def home(request):
    sessions = SessionEntry.objects.all()
    return render(request, 'home.html', {'sessions': sessions})

def library(request):
    exercises = Exercise.objects.all()
    return render(request, 'library.html', {'exercises': exercises})
