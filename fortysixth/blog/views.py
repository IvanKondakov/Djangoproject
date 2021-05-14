from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.models import User
from .forms import BlogForm
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from loguru import logger

@login_required
def blog(request):
    blog = Blog.objects.order_by('-created_at')
    return render(request, 'blog/blog.html', {'blog': blog})

class BlogDetailView(ListView):
    model = Blog
    ordering = ['-created_at']
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

class DetailView(DetailView):
    model = Blog
    template_name = 'blog/details_view.html'
    context_object_name = 'blog'

class BlogUpdateView(UpdateView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog/update.html'
    context_object_name = 'blog'
    form_class = BlogForm
    success_url = '/blog/'

class BlogCreateView(CreateView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog/create.html'
    context_object_name = 'blog'
    form_class = BlogForm
    success_url = '/blog/'

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'
