from bookshelf.models import Book

# Retrieve and delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)

# Expected Output:
# (1, {'bookshelf.Book': 1})
# <QuerySet []>