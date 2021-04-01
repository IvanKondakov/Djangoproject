from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from aft.models import Profile
from django.forms import ModelForm, TextInput, Textarea, Select, CharField, EmailInput, FileInput, DateInput

class EditProfileForm(ModelForm):
    #last_login = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'class':'form-control'}))
    #date_joined = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'class':'form-control'}))
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
        fields = ['bio', 'location', 'website', 'phone', 'age', 'degree', 'birth_date', 'profile_pic', 'status']
        widgets = {
            "bio": Textarea(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 730px',
            }),
            "location": TextInput(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 200px',
            }),
            "website": TextInput(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 200px',
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 200px',
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 200px',
            }),
            "degree": TextInput(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 200px',
            }),
            "birth_date": DateInput(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 200px',
            }),
            "status": TextInput(attrs={
                'class': 'form-control',
                'style': 'display: inline; width: 200px',
            }),
            "profile_pic": FileInput(attrs={
            'style': 'margin-top: 20px',
            }),

        }
