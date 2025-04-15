from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Twix(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_At}"
