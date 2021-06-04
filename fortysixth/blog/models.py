from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('feed')

class Blog(models.Model):
    title = models.CharField('Название', max_length=50)
    desc = models.CharField('Описание', max_length=100)
    full_text = QuillField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null = True, blank=True, upload_to= "images/")
    category = models.CharField(max_length=255, default='other')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_lkes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
