# Djangoproject
Hello everyone, this is my first Django project.
## Version 0.1
### ***App's:***
1. main: url's and views for main pages
2. blog: work with blog posts
3. aft: register application
> main app
> 
url's:
```python
    path('', views.default, name= 'redirect'),
    path('profile/', views.index, name='home'),
    path('edit_profile/', login_required(views.UserEditView.as_view()), name='edit_profile'),
    path('<int:pk>/about/', login_required(views.about.as_view()), name='about'),
    path('<int:pk>/edit/about/', login_required(views.edit_about.as_view()), name='about_edit'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
```
> blog app
> 
url's:
```python
    path('', login_required(views.BlogDetailView.as_view()), name='blog'),
    path('create', views.blog_create, name='create'),
    path('<int:pk>/update', login_required(views.BlogUpdateView.as_view()), name='blog_update'),
    path('<int:pk>/delete', login_required(views.BlogDeleteView.as_view()), name='blog_delete'),
```
model:
```python
class Blog(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = QuillField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null = True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
```
views:
```python
@login_required
def blog(request):
    blog = Blog.objects.order_by('-created_at')
    return render(request, 'blog/blog.html', {'blog': blog})
    
    class BlogDetailView(ListView):
    model = Blog
    paginate_by = 3
    ordering = ['-created_at']
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

class BlogUpdateView(UpdateView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog/update.html'
    context_object_name = 'blog'
    form_class = BlogForm
    success_url = '/blog/'

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'


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
```
> aft app
> 
urls:
```python
    path('', include('django.contrib.auth.urls'), name='home'),
    path('sign_up/',views.sign_up,name="sign-up"),
    path('account_activation_sent/',views.account_activation_sent, name='account_activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate')
```
models:
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key = True)
    bio = models.TextField(max_length=1000, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    age =  models.CharField(max_length=30, blank=True)
    degree =  models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    status =  models.CharField(max_length=30, blank=True)
    email_confirmed = models.BooleanField(default=False)
    profile_pic = models.ImageField(null = True, blank=True, upload_to= "images/profile")

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

```
views:
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key = True)
    bio = models.TextField(max_length=1000, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    age =  models.CharField(max_length=30, blank=True)
    degree =  models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    status =  models.CharField(max_length=30, blank=True)
    email_confirmed = models.BooleanField(default=False)
    profile_pic = models.ImageField(null = True, blank=True, upload_to= "images/profile")

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

```
