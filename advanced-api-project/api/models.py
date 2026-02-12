from django.db import models

# Create your models here.
# This file defines the data models for the API application. It includes an Author model and a Book model, 
# where each book is associated with an author. The Author model has a name field, while the Book model has fields for title, publication year,
#  and a foreign key linking it to an Author.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    
