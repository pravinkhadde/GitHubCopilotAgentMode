
from django.contrib import admin
from .models import WorkoutSuggestion

@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
	list_display = ('user', 'title', 'difficulty', 'created_at')
