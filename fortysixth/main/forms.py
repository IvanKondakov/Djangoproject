from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, MultiWidget


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'fadeIn second',
                'name': 'login',
                'id': 'login',
                'placeholder': 'username'
            }),
            "password": TextInput(attrs={
                    'class': 'fadeIn third',
                    'name': 'login',
                    'id': 'password',
                    'placeholder': 'password'
            })
        }
