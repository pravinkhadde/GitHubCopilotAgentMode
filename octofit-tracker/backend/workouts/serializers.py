from rest_framework import serializers
from .models import WorkoutSuggestion

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'user', 'user_username', 'title', 'description', 'exercises', 'duration', 'difficulty', 'created_at']