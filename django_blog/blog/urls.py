from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from django.contrib.auth import views as auth_views
from . import views as user_views
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # Custom Views
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    
    # Built-in Auth Views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]