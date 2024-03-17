from django import forms
from .models import BorrowedBook

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['book', 'return_date']  # Fields to be displayed in the form
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'})  # Using DateInput widget for return date
        }
