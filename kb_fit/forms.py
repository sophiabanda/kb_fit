from django import forms
from .models import Exercise, SessionEntry

class ExerciseForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())
    reps = forms.IntegerField()
    sets = forms.IntegerField()
    time = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter notes for time', 'size': '20'}))

    class Meta:
        model = Exercise
        fields = ['exercise', 'reps', 'sets', 'time']

class CombinedForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    program_info = forms.CharField()
    hrv = forms.IntegerField()
    rpe = forms.IntegerField()
    notes = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SessionEntry
        fields = ['date', 'program_info', 'hrv', 'rpe', 'notes']