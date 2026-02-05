from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager



    



# Create your models here.
class CustomUser(AbstractUser):
    """Custom user extending Django's AbstractUser.

    Includes optional `date_of_birth` and `profile_photo` fields used
    by the admin configuration.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    def __str__(self):
        return self.title
    class Meta:
        permissions = [
            ("can_view", "can view book details"),
            ("can_create","can create new book"),
            ("can_edit","can edit book details"),
            ("can_delete","can delete book details")

        ]