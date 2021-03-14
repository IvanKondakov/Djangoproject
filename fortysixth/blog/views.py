from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib import messages
from django.views.generic import DetailView


def blog(request):
    blog = Blog.objects.order_by('-created_at')
    return render(request, 'blog/blog.html', {'blog': blog})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/details_view.html'
    context_object_name = 'blog'

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
