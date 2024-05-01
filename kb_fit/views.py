from django.shortcuts import render, redirect
from .models import Exercise, SessionEntry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.forms import formset_factory
from .forms import ExerciseForm, CombinedForm
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
    
ExerciseFormSet = formset_factory(ExerciseForm, extra=10)

@login_required
def session_create(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        exercise_formset = ExerciseFormSet(request.POST, prefix='exercises')
        if form.is_valid() and exercise_formset.is_valid():
            session_entry = form.save(commit=False)
            session_entry.user = request.user
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
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
