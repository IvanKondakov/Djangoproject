from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class UserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
                'class': 'fadeIn third',
                'placeholder': 'type your pass',
                'data-toggle': 'tooltip',
                'data-placement': 'left',
                'title': "Your password can’t be too similar to your other personal information. \n Your password must contain at least 8 characters. \n Your password can’t be a commonly used password. \n Your password can’t be entirely numeric."})
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
                'class': 'fadeIn third',
                'placeholder': 'confirm it',
                'data-toggle': 'tooltip',
                'data-placement': 'left',
                'title': "Enter the same password as before, for verification."})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            "username": TextInput(attrs={
                'class': 'fadeIn first',
                'placeholder': 'login',
                'data-toggle': 'tooltip',
                'data-placement': 'left',
                'title': "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            }),
            "email": EmailInput(attrs={
                    'class': 'fadeIn second',
                    'placeholder': '@',
                    'data-toggle': 'tooltip',
                    'data-placement': 'left',
                    'title': "Required. Inform a valid email address.",
            })
        }

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('birth_date', 'bio')
