import os
import django
from relationship_app.models import Author, Book, Library, Librarian
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()
def query_book(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)
def list_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()
def retrieve_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

if __name__ == "__main__":
    pass
