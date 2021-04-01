from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from aft.models import Profile
from blog.models import Blog
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm, ProfileForm

@login_required
def index(request):
    return render(request, 'main/index.html')

@login_required
def default(request):
    return redirect('home')

class about(DetailView):
    model = Profile
    template_name= 'main/about.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(about, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, user_id = self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class edit_about(UpdateView):
    model = Profile
    template_name= 'main/edit_about.html'
    success_url ='/profile/'
    form_class = ProfileForm
    #fields = ['bio', 'location', 'website', 'phone', 'age', 'degree', 'birth_date', 'profile_pic', 'status']

@login_required
def resume(request):
    return render(request, 'main/resume.html')

@login_required
def portfolio(request):
    return render(request, 'main/portfolio.html')

@login_required
def contact(request):
    return render(request, 'main/contact.html')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'main/edit_profile.html'
    context_object_name = 'profile'
    success_url ='/profile/'
    queryset = Profile.objects.all()

    def get_object(self):
        return self.request.user
