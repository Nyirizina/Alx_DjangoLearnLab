from django.urls import path
from .models import Book
from . import views

urlpatterns = [
    path('books/', views.BookListCreateAPIView.as_view(), name='book-list'),
]