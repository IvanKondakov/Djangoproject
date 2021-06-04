from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from aft.models import Profile
from django.forms import ModelForm, TextInput, Textarea, Select, CharField, EmailInput, FileInput, DateInput

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',  'last_name']
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
            }),
            "email": EmailInput(attrs={
                    'class': 'form-control',
            })
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'website', 'phone', 'age', 'birth_date', 'profile_pic']
        widgets = {
            "bio": Textarea(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 730px',
            }),
            "location": TextInput(attrs={
                'class': 'form-control',
            }),
            "website": TextInput(attrs={
                'class': 'form-control',
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
            }),
            "birth_date": DateInput(attrs={
                'class': 'form-control',
            }),
            "profile_pic": FileInput(attrs={
            'style': 'margin-top: 0px',
            }),

        }
