from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default="NOT DESCRIPTION")

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)
