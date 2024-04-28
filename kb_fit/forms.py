from django.forms import ModelForm
from .models import Exercise, SessionEntry

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'types']