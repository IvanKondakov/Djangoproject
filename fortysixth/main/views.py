from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def resume(request):
    return render(request, 'main/resume.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def contact(request):
    return render(request, 'main/contact.html')

def sign_up(request):
    context = {}
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'main/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)
