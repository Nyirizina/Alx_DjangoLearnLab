from django.test import TestCase
from .models import Book
from rest_framework.test import APITestCase
from rest_framework import status

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title="Kugasima", author="Bushali", publication_year=2019)
        Book.objects.update(id=1,title="twagiye", author="bthrey", publication_year=2022)
        Book.objects.create(title="twagiye", author="bthrey", publication_year=2022)
