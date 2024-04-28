from django.contrib import admin
from .models import Exercise, Photo, SessionEntry, ExerciseType

admin.site.register([Exercise, Photo, SessionEntry, ExerciseType])

