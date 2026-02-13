from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import permissions

# API view for listing and creating authors
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.filter(book = 'id')
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.create()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.update()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.delete()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



