from .forms import UserForm, ProfileForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .tokens import account_activation_token
from loguru import logger
from .bot_log import tel_bot_logs
from django.http import HttpResponse
from .models import Profile

def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profileform = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            logger.info(user)
            user.is_active = False
            user.save()
            profileform = form.save(commit=False)
            profileform.is_active = False
            profileform.save()
            current_site = get_current_site(request)
            logger.info(current_site)
            subject = 'Activate Your MySite Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10:00")
            logger.info(message)
            tel_bot_logs(message)
            return redirect('account_activation_sent')
    else:
        form = UserForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
        logger.info(user)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('blog')
    else:
        return render(request, 'registration/account_activation_invalid.html')

def complete(request):
    username = request.GET.get("username", "")
    hash = request.GET.get("hash", "")
    hash= urlsafe_base64_encode(force_bytes(hash))
    userpic = request.GET.get("photo_url", "")
    user = User.objects.create(username = username, password = hash)
    login(request, user)
    user.save()

    user_id = User.objects.get(username = username)
    profile = Profile.objects.get(user = user_id.id)
    profile.tg_pic = userpic
    profile.save()

    return redirect('blog')
