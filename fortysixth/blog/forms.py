from .models import Blog
from django.forms import ModelForm, TextInput, Textarea


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'id': 'exampleFormControlInput1'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text',
                'id': "exampleFormControlTextarea1"
            })
        }

