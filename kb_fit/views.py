from django.shortcuts import render, redirect
from .models import Exercise, SessionEntry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.forms import formset_factory
from .forms import ExerciseForm, CombinedForm

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
    
ExerciseFormSet = formset_factory(ExerciseForm, extra=10)

def session_create(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        exercise_formset = ExerciseFormSet(request.POST, prefix='exercises')
        if form.is_valid() and exercise_formset.is_valid():
            session_entry = form.save(commit=False)
            session_entry.save()
            for exercise_form in exercise_formset:
                exercise = exercise_form.save(commit=False)
                exercise.session_entry = session_entry
                exercise.save()
            return redirect('session_detail', pk=session_entry.id)
        else:
            print(form.errors)
            print(exercise_formset.errors)
    else:
        form = CombinedForm()
        exercise_formset = ExerciseFormSet(prefix='exercises')
    return render(request, 'session_create.html', {'form': form, 'exercise_formset': exercise_formset})