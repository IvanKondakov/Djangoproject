from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create', views.blog_create, name='create'),
]
