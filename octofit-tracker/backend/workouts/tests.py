
from django.test import TestCase
from django.contrib.auth.models import User
from .models import WorkoutSuggestion

class WorkoutSuggestionTestCase(TestCase):
	def test_workout_suggestion_creation(self):
		user = User.objects.create_user(username='testuser4', password='testpass')
		workout = WorkoutSuggestion.objects.create(
			user=user,
			title='Super Strength',
			description='Strength workout',
			exercises=[{"name": "Pushup", "sets": 3, "reps": 10}],
			duration=45,
			difficulty='beginner'
		)
		self.assertEqual(workout.title, 'Super Strength')
