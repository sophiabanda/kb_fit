from django.contrib import admin
from .models import Exercise, SessionEntry, ExerciseType, SessionExercise, SessionWarmup, Warmup

admin.site.register([Exercise, SessionEntry, ExerciseType, Warmup, SessionExercise, SessionWarmup])

