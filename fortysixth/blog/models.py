from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField('Название', max_length=50)
    desc = models.CharField('Описание', max_length=100)
    full_text = QuillField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null = True, blank=True, upload_to= "images/")
    No = models.CharField('No', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
