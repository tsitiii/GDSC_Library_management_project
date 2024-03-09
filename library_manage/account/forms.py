from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User


class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

class SignUpForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    email=forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    class meta:
        model= User
        fields=('username','email', 'password1', 'password2', 'Is super admin', 'Is admin', 'Is student')
    



    