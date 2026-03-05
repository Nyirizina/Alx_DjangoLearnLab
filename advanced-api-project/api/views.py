from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# API view for listing and creating authors
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']
    ordering = ['title']  # Default ordering by publication year



    def get_queryset_title(self):
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = Book.objects.filter(title=title)
        return queryset
    def get_queryset_publication_year(self):
        publication_year = self.request.query_params.get('publication_year', None)
        if publication_year is not None:
            queryset = Book.objects.filter(publication_year=publication_year)
        return queryset
    def get_queryset_author(self):
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = Book.objects.filter(author=author)
        return queryset
    


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.filter(book = 'id')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.create()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.update()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.delete()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



