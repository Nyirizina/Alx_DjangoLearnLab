from django.test import TestCase
from .models import Book, Author
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse


class BookAPITest(TestCase):
    #CREATE USER FOR TESTING
    #function to set up test data before each test method is run
    def setUp(self):
        #create user authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        #create author and book for testing
        self.author =Author.objects.create(name='Menama')
        self.book = Book.objects.create(title='Mugenzde', pubication_year=1030, author=self.author)

        #define urls for API endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

#test method to verify that the book list endpoint is accessible and returns the correct data
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')
    #test method to verify that unauthenticated users cannot create a book
    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Unwanted Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #test method to verify that authenticated users can update a book's details
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Updated Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    
    def test_filter_books_by_year(self):
        response = self.client.get(self.list_url, {'publication_year': 1030})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Mugenzde')

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {'search': 'New book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'New Book')
    
    def test_ordering_books(self):
        """
        Test ordering books by publication year.
        """
        Book.objects.create(title="Book A", publication_year=2000, author=self.author)
        Book.objects.create(title="Book B", publication_year=1990, author=self.author)
        
        # Order by year ascending
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check first item is the oldest (1937 Hobbit from setUp)
        self.assertEqual(response.data[0]['publication_year'], 1937)
        # Check last item is the newest (2000)
        self.assertEqual(response.data[-1]['publication_year'], 2000)


