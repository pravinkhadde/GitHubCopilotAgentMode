
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Activity

class ActivityTestCase(TestCase):
	def test_activity_creation(self):
		user = User.objects.create_user(username='testuser2', password='testpass')
		activity = Activity.objects.create(user=user, activity_type='running', duration=30)
		self.assertEqual(activity.activity_type, 'running')
