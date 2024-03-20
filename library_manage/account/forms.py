from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User


class LoginForm(forms.Form):
    username=forms.CharField()

    password=forms.CharField(
        widget=forms.PasswordInput(
            # attrs={"class": "form-control"} it is used if want custom styling for this field
        )
    )

class SignUpForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
        #     # attrs={"class": "form-control"}
        )
    )

    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
        attrs={"class": "form-control"}
        )
     )
    class Meta:
        model= User
        fields=('username','email', 'password1', 'password2', 'is_superuser', 'is_admin', 'is_student')
    



    
