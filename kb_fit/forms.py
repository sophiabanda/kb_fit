from django import forms
from .models import Exercise, SessionEntry

class ExerciseForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())
    reps = forms.IntegerField()
    sets = forms.IntegerField()
    time = forms.TimeField()

    class Meta:
        model = Exercise
        fields = ['exercise', 'reps', 'sets', 'time']

class CombinedForm(forms.ModelForm):
    date = forms.DateField()
    program_info = forms.CharField()
    hrv = forms.IntegerField()
    rpe = forms.IntegerField()
    notes = forms.CharField()

    class Meta:
        model = SessionEntry
        fields = ['date', 'program_info', 'hrv', 'rpe', 'notes']