from django.contrib import admin
from django.urls import path
from .views import SignUpView, list_books, LibraryDetailView 
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
]
