from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.BlogDetailView.as_view()), name='blog'),
    path('create', login_required(views.BlogCreateView.as_view()), name='create'),
    path('<int:pk>', views.DetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update', login_required(views.BlogUpdateView.as_view()), name='blog_update'),
    path('<int:pk>/delete', login_required(views.BlogDeleteView.as_view()), name='blog_delete'),
]
