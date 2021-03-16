from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
