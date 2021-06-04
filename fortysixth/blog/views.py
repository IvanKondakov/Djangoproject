from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category
from django.contrib.auth.models import User
from .forms import BlogForm
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from loguru import logger
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))
    blog.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))

def CategoryView(request, cats):
    category_blogs = Blog.objects.filter(category = cats)
    return render(request, 'blog/category.html', {'cats': cats, 'category_blogs': category_blogs})

class BlogDetailView(ListView):
    model = Blog
    ordering = ['-created_at']
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

class FeedDetailView(ListView):
    model = Blog
    ordering = ['-created_at']
    template_name = 'blog/feed.html'
    context_object_name = 'blog'

class DetailView(DetailView):
    model = Blog
    template_name = 'blog/details_view.html'
    context_object_name = 'blog'

    def  get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Blog, id=self.kwargs['pk'])
        total_lkes = stuff.total_lkes()
        context["total_lkes"] = total_lkes
        return context

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
