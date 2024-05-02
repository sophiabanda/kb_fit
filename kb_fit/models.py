from django.db import models
from django.contrib.auth.models import User

TYPES = (
    ('C', 'Cardio'),
    ('S', 'Strength'),
    ('M', 'Mobility'),
    ('R', 'Recovery'),
    ('W', 'Warmup'),
    ('O', 'Other')
)

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    types = models.ManyToManyField('ExerciseType')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Warmup(models.Model):
    name = models.CharField(max_length=100)
    types = models.ManyToManyField('ExerciseType')

    def __str__(self):
        return self.name

class ExerciseType(models.Model):
    name = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return self.get_name_display()

class SessionEntry(models.Model):
    date = models.DateField('Session Date')
    hrv = models.IntegerField(null=True, blank=True)
    program_info = models.CharField(max_length=150, null=True, blank=True)
    warmups = models.ManyToManyField(Warmup, through='SessionWarmup', related_name='warmup_sessions')
    exercises = models.ManyToManyField(Exercise, through='SessionExercise', related_name='exercise_sessions')
    rpe = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Session Entry {self.id} on {self.date}"
    
class SessionExercise(models.Model):
    session = models.ForeignKey('SessionEntry', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField(null=True, blank=True, default=0)
    sets = models.IntegerField(null=True, blank=True, default=0)
    time = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.exercise.name} in session {self.session.id}"

class SessionWarmup(models.Model):
    session = models.ForeignKey('SessionEntry', on_delete=models.CASCADE)
    warmup = models.ForeignKey(Warmup, on_delete=models.CASCADE)
    reps = models.IntegerField(null=True, blank=True, default=0)
    sets = models.IntegerField(null=True, blank=True, default=0)
    time = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.warmup.name} in session {self.session.id}"
