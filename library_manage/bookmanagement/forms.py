from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'book_cover',  'ratings', 'status']
        # 'book_file', can be added if online pdf reading feature is wanted