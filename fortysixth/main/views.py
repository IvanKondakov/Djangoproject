from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from aft.models import Profile
from blog.models import Blog, Category
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from loguru import logger
from .forms import EditProfileForm, ProfileForm


def  follow_unfollow_profile(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('blog')

def  follow_unfollow_category(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('category_str')
        obj = Category.objects.get(name=pk)

        if obj in my_profile.following_category.all():
            my_profile.following_category.remove(obj)
        else:
            my_profile.following_category.add(obj)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('blog')

@login_required
def default(request):
    return redirect('blog')

class about(DetailView):
    model = Profile
    template_name= 'main/about.html'

    def get_object(self, **kwargs):
        pk = self.kwargs['pk']
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(about, self).get_context_data(*args, **kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user = self.request.user)
        page_user = get_object_or_404(Profile, user_id = self.kwargs['pk'])
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["page_user"] = page_user
        context["follow"] = follow
        return context

class edit_about(UpdateView):
    model = Profile
    template_name= 'main/edit_about.html'
    form_class = ProfileForm
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("about", kwargs={"pk": pk})

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'main/edit_profile.html'
    context_object_name = 'profile'
    success_url ='/profile/'
    queryset = Profile.objects.all()

    def get_object(self):
        return self.request.user
