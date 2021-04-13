from .models import Blog
from django.forms import ModelForm, TextInput, Textarea, Select


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'full_text', 'author', 'image', 'desc']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'id': 'exampleFormControlInput1'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text',
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'value': "",
                'id': "au",
                'type': "hidden"
            }),
            "desc": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'id': 'exampleFormControlInput1'
            }),
        }
