from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.BlogDetailView.as_view()), name='blog'),
    path('feed', login_required(views.FeedDetailView.as_view()), name='feed'),
    path('create', login_required(views.BlogCreateView.as_view()), name='create'),
    path('<int:pk>', views.DetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update', login_required(views.BlogUpdateView.as_view()), name='blog_update'),
    path('<int:pk>/delete', login_required(views.BlogDeleteView.as_view()), name='blog_delete'),
    path('category/<str:cats>/', login_required(views.CategoryView), name='category'),
    path('like/<int:pk>', login_required(views.LikeView), name='like_post'),
]
