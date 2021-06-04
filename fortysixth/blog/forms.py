from .models import Blog, Category
from django.forms import ModelForm, TextInput, Textarea, Select

choices = Category.objects.all().values_list('name','name')
choices_list = []

for item in choices:
    choices_list.append(item)

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'full_text', 'author', 'image', 'desc', 'category']

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
            "category": Select(choices = choices_list, attrs={
                'class': 'form-control',
                'placeholder': 'Category',
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
