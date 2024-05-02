from django import forms
from django.forms import inlineformset_factory
from .models import Exercise, Warmup, SessionEntry, SessionExercise, SessionWarmup

class SessionExerciseForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())
    reps = forms.IntegerField(required=False)
    sets = forms.IntegerField(required=False)
    time = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Note your time', 'size': '20'}))

    class Meta:
        model = SessionExercise
        fields = ['exercise', 'reps', 'sets', 'time']

class SessionWarmupForm(forms.ModelForm):
    warmup = forms.ModelChoiceField(queryset=Warmup.objects.all())
    reps = forms.IntegerField(required=False)
    sets = forms.IntegerField(required=False)
    time = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Note your time', 'size': '20'}))

    class Meta:
        model = SessionWarmup
        fields = ['warmup', 'reps', 'sets', 'time']

SessionExerciseFormSet = inlineformset_factory(SessionEntry, SessionExercise, form=SessionExerciseForm, extra=1, can_delete=True)
SessionWarmupFormSet = inlineformset_factory(SessionEntry, SessionWarmup, form=SessionWarmupForm, extra=1, can_delete=True)

class CombinedForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    program_info = forms.CharField(required=False)
    hrv = forms.IntegerField(required=False)
    rpe = forms.IntegerField(required=False)
    notes = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = SessionEntry
        fields = ['date', 'program_info', 'hrv', 'rpe', 'notes']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.exercises_formset = SessionExerciseFormSet(*args, **kwargs, instance=self.instance)
        self.warmups_formset = SessionWarmupFormSet(*args, **kwargs, instance=self.instance)

    def is_valid(self):
        return super().is_valid() and self.exercises_formset.is_valid() and self.warmups_formset.is_valid()

    def save(self, commit=True):
        self.instance.user = self.user
        saved_instance = super().save(commit=commit)
        self.exercises_formset.instance = saved_instance
        self.warmups_formset.instance = saved_instance
        self.exercises_formset.save()
        self.warmups_formset.save()
        return saved_instance
