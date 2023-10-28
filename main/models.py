from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1)
    name = models.CharField(max_length=255)
    bio_data = models.TextField(blank=True) #optional
    preferred_genre = models.CharField(max_length=100, blank=True) #optional