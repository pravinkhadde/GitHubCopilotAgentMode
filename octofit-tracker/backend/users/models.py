
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
	ROLE_CHOICES = [
		('student', 'Student'),
		('teacher', 'Gym Teacher'),
	]
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
	age = models.PositiveIntegerField(null=True, blank=True)
	weight = models.FloatField(null=True, blank=True)
	height = models.FloatField(null=True, blank=True)
	fitness_level = models.CharField(max_length=20, choices=[
		('beginner', 'Beginner'),
		('intermediate', 'Intermediate'),
		('advanced', 'Advanced'),
	], default='beginner')
	def __str__(self):
		return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()
