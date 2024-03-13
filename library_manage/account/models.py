from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    is_admin=models.BooleanField('Is admin', default=False)
    is_student=models.BooleanField('Is student', default=False)
    is_super_admin=models.BooleanField('Is super admin', default=False)
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=150, unique=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

User = get_user_model()



class Book(models.Model):
    # Define your book fields here
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    # Add other fields as necessary

    def __str__(self):
        return self.title
  