from django.shortcuts import render, redirect
from .models import Exercise, SessionEntry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.forms import formset_factory
from .forms import CombinedForm, SessionExerciseForm, SessionWarmupForm
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    sessions = SessionEntry.objects.all()
    return render(request, 'home.html', {'sessions': sessions})

@login_required
def sessions(request):
    sessions = SessionEntry.objects.filter(user=request.user)
    return render(request, 'sessions.html', {'sessions': sessions})

class ExerciseList(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'

class SessionDetail(DetailView):
    model = SessionEntry
    template_name = 'session_detail.html'
    context_object_name = 'session'


SessionExerciseFormSet = formset_factory(SessionExerciseForm, extra=1)
SessionWarmupFormSet = formset_factory(SessionWarmupForm, extra=1)

@login_required
def session_create(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST, user=request.user)
        print(form.is_valid())
        exercise_formset = SessionExerciseFormSet(request.POST, prefix='exercises')
        print(exercise_formset.is_valid())
        warmup_formset = SessionWarmupFormSet(request.POST, prefix='warmups')
        print(warmup_formset.is_valid())
        session_entry = form.save()
        print('session entry: ', session_entry)
        for exercise_form in exercise_formset:
            if exercise_form.has_changed():
                exercise = exercise_form.save(commit=False)
                exercise.session = session_entry
                exercise.save()
                print('exercise: ', exercise)
        for warmup_form in warmup_formset:
            if warmup_form.has_changed():
                warmup = warmup_form.save(commit=False)
                warmup.session = session_entry
                warmup.save()
                print('warmup: ', warmup)
        return redirect('session_detail', pk=session_entry.id)
     
    else:
        form = CombinedForm(user=request.user)
        exercise_formset = SessionExerciseFormSet(prefix='exercises')
        warmup_formset = SessionWarmupFormSet(prefix='warmups')
    return render(request, 'session_create.html', {'form': form, 'exercise_formset': exercise_formset, 'warmup_formset': warmup_formset})


class SessionUpdate(LoginRequiredMixin, UpdateView):
    model = SessionEntry
    fields = '__all__'

    def get_success_url(self):
        return reverse('session_detail', args=[str(self.object.id)])

class SessionDelete(LoginRequiredMixin, DeleteView):
    model = SessionEntry
    success_url = '/sessions/'

class ExerciseCreate(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ['name', 'types']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.user = self.request.user
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('library')
    
class ExerciseDelete(LoginRequiredMixin, DeleteView):
    model = Exercise

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('library') 
    
class ExerciseDetail(LoginRequiredMixin, DetailView):
    model = Exercise
    context_object_name = 'exercise'

class ExerciseUpdate(LoginRequiredMixin, UpdateView):
    model = Exercise
    fields = ['name', 'types']

    def get_success_url(self):
        return reverse('library')
    
def signup(request):
    error_message = ''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid signup - try again'
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
