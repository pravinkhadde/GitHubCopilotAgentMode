from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from activities.models import Activity
from django.db.models import Sum
from django.contrib.auth.models import User

class LeaderboardView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Get total calories burned by each user
        leaderboard = Activity.objects.values('user__username').annotate(
            total_calories=Sum('calories_burned')
        ).order_by('-total_calories')[:10]  # Top 10
        
        return Response(leaderboard)
