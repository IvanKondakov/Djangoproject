from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class QuillPostAdmin(admin.ModelAdmin):
    pass
