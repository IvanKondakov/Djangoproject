from . import views
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='home'),
    path('sign_up/',views.sign_up,name="sign-up"),
    path('account_activation_sent/',views.account_activation_sent, name='account_activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate')
]
