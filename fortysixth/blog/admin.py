from django.contrib import admin
from .models import Blog, Category


@admin.register(Blog)
@admin.register(Category)
class QuillPostAdmin(admin.ModelAdmin):
    pass
