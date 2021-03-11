from django.shortcuts import render


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