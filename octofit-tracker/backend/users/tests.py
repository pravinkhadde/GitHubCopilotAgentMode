
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTestCase(TestCase):
	def test_user_profile_creation(self):
		user = User.objects.create_user(username='testuser', password='testpass')
		profile = UserProfile.objects.get(user=user)
		self.assertEqual(profile.role, 'student')
