from django.db import models
from django.utils import timezone

class User(models.Model):
    COURSE_TYPE = [
        ('B', 'Bachelor'),
        ('M', 'Master'),
        ('PHD', 'PhD'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    type = models.CharField(max_length=3, choices=COURSE_TYPE)
    time = models.DateTimeField(default=timezone.now)  # Callable, not function call
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# one to many relationship
class UserSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.skill_name} ({self.user.name})'
    
# many to many relationship

class UserData(models.Model):
    userData = models.ManyToManyField(User, related_name='users')
    def __str__(self):
        return self.user.name