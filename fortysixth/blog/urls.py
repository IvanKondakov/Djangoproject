from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create', views.blog_create, name='create'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update', views.BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog_delete'),
]
