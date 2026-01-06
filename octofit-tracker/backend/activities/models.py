from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('weightlifting', 'Weightlifting'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.FloatField(null=True, blank=True)
    distance = models.FloatField(null=True, blank=True, help_text="Distance in km")
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date.date()}"
