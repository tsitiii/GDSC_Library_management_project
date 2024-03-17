from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    rating = forms.ChoiceField(
        label='Rating',
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']
