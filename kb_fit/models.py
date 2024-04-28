from django.db import models

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

    def __str__(self):
        return self.name

class ExerciseType(models.Model):
    name = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return self.get_name_display()

class Photo(models.Model):
    url = models.CharField(max_length=200)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for exercise_id: {self.exercise_id} @{self.url}"

class SessionEntry(models.Model):
    date = models.DateField('Session Date')
    hrv = models.IntegerField()
    program_info = models.CharField(max_length=150)
    warmup = models.ManyToManyField(Exercise, related_name='warmup_sessions')
    exercise = models.ManyToManyField(Exercise, related_name='exercise_sessions')
    rpe = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return f"Session Entry {self.id} on {self.date}"
