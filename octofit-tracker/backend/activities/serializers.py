from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_username', 'activity_type', 'duration', 'calories_burned', 'distance', 'date', 'notes']