from django.db import models
from django.contrib.auth.models import User

class WorkoutSuggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    exercises = models.JSONField()  # List of exercises with sets, reps, etc.
    duration = models.PositiveIntegerField(help_text="Estimated duration in minutes")
    difficulty = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} for {self.user.username}"
