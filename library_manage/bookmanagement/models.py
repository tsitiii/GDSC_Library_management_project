from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    status_choices = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='available')

    def __str__(self):
        return self.title
