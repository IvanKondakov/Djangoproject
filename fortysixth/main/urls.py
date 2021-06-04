from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.default, name= 'default'),
    path('edit_profile/', login_required(views.UserEditView.as_view()), name='edit_profile'),
    path('<int:pk>/about/', login_required(views.about.as_view()), name='about'),
    path('<int:pk>/edit/about/', login_required(views.edit_about.as_view()), name='about_edit'),
]
