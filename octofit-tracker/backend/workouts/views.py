from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import WorkoutSuggestion
from .serializers import WorkoutSuggestionSerializer

class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSuggestionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return WorkoutSuggestion.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
