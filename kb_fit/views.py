from django.shortcuts import render
from .models import Exercise, SessionEntry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

def home(request):
    sessions = SessionEntry.objects.all()
    return render(request, 'home.html', {'sessions': sessions})

def sessions(request):
    sessions = SessionEntry.objects.all()
    return render(request, 'sessions.html', {'sessions': sessions})

class ExerciseList(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'

class SessionDetail(DetailView):
    model = SessionEntry
    template_name = 'session_detail.html'
    context_object_name = 'session'

class SessionCreate(CreateView):
    model = SessionEntry
    template_name = 'kb_fit/session_form.html'
    fields = '__all__'