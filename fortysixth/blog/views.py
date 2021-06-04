from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category
from django.contrib.auth.models import User
from .forms import BlogForm
from aft.models import Profile
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from loguru import logger
from django.http import HttpResponseRedirect
from itertools import chain
import sys

def LikeView(request, pk):
    blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))
    liked = False
    if blog.likes.filter(id = request.user.id).exists():
        blog.likes.remove(request.user)
        liked = False
    else:
        blog.likes.add(request.user)
        liked = False

    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))

def CategoryView(request, cats):
    category_blogs = Blog.objects.filter(category = cats)
    return render(request, 'blog/category.html', {'cats': cats, 'category_blogs': category_blogs})

class BlogDetailView(ListView):
    model = Blog
    ordering = ['-created_at']
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

def FeedDetailView(request):
    all = Blog.objects.all()
    profile = Profile.objects.get(user=request.user)
    users = [user for user in profile.following.all()]
    categories = [category for category in profile.following_category.all()]
    cats = []
    blogs = []
    qs = None
    ss = None

    for u in users:
        if u != profile:
            b_blogs = Blog.objects.filter(author=u)
            blogs.append(b_blogs)

    if len(blogs) > 0 :
        qs = sorted(chain(*blogs), reverse=True, key=lambda obj: obj.created_at)

    for c in categories:
        bb_blogs = Blog.objects.filter(category=c)
        cats.append(bb_blogs)

    if len(cats) > 0 :
        ss = sorted(chain(*cats), reverse=True, key=lambda obj: obj.created_at)

    return render(request, 'blog/feed.html' , {'sub': qs, 'blog': all, 'cats': ss})

class DetailView(DetailView):
    model = Blog
    template_name = 'blog/details_view.html'
    context_object_name = 'blog'

    def  get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Blog, id=self.kwargs['pk'])
        total_lkes = stuff.total_lkes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id ).exists():
            liked = True

        profile = Profile.objects.get(user=self.request.user)
        users = [user for user in profile.following.all()]
        author = stuff.author
        follow = False
        if author in users:
            follow = True

        categories= [category for category in profile.following_category.all()]
        category = stuff.category

        follow_category = False
        for el in categories:
            some = str(el)
            if category == some:
                follow_category = True

        context["total_lkes"] = total_lkes
        context["liked"] = liked
        context["follow"] = follow
        context["follow_category"] = follow_category

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
