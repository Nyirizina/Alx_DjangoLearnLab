from django.urls import path
from .models import Book
from . import views
from .urls import router
from django.urls import include

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

urlpatterns = [
    path('books/', views.BookListCreateAPIView.as_view(), name='book-list'),
    path('books/list/', views.BookList.as_view(), name='book-list-only'),
    path('books/<int:pk>/', views.BookViewSet.as_view(), name='book-detail'),
    path('', include(router.urls)),
    
]