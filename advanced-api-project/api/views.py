from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated
# API view for listing and creating authors
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.filter(book = 'id')
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.create()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.update()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.delete()
    serializer_class = BookSerializer



