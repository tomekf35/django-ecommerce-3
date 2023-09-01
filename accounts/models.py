from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to="avatars/", blank=True)
    about = models.TextField(blank=True)
    social_media = models.JSONField(blank=True, null=True)

    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.username
