from django.db import models
from django.contrib.auth.models import AbstractUser


# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # symmetrical=False is key for follow relationships
    following = models.ManyToManyField(
        'self', 
        related_name='followers', 
        symmetrical=False, 
        blank=True
    )

    def __str__(self):
        return self.username
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    



