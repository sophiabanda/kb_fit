from django.shortcuts import render
from .models import Exercise, SessionEntry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

def home(request):
    sessions = SessionEntry.objects.all()
    return render(request, 'home.html', {'sessions': sessions})

class ExerciseList(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'

