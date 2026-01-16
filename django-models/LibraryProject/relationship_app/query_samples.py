import os
import django
from relationship_app.models import Author, Book, Library, Librarian
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()
def query_book(muhizi):
    author = Author.objects.get(name='Muhizi')
    return Book.objects.filter(author=author)
def list_library(Ububiko):
    library = Library.objects.get(name='Ububiko')
    return library.books.all()
def retrieve_librarian(Ububiko):
    library = Library.objects.get(name='Ububiko')
    return library.librarian
