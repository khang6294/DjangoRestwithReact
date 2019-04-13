from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional info

    nickname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username


