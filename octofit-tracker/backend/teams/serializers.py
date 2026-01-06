from rest_framework import serializers
from .models import Team
from django.contrib.auth.models import User

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_by', 'created_by_username', 'members', 'created_at']