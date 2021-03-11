from django.db import models


class Blog(models.Model):
    title = models.CharField('Название', max_length=50)
    intro = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
