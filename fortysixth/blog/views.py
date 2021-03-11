from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib import messages


def blog(request):
    blog = Blog.objects.order_by('-created_at')
    return render(request, 'blog/blog.html', {'blog': blog})


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            messages.info(request, "Not correct")



    form = BlogForm()

    data = {
        'form': form
    }
    return render(request, 'blog/create.html', data)