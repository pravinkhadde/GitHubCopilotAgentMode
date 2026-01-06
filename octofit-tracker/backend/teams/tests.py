
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team

class TeamTestCase(TestCase):
	def test_team_creation(self):
		user = User.objects.create_user(username='testuser3', password='testpass')
		team = Team.objects.create(name='Avengers', created_by=user)
		team.members.add(user)
		self.assertEqual(team.name, 'Avengers')
