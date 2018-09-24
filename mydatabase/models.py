from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmailObject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    change = models.BooleanField(default=False)
    create_data = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_data']


    def __str__(self):
        return self.name
