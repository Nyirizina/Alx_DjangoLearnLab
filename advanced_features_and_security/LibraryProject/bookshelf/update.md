from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update and save
book.title = "Nineteen Eighty-Four"
book.save()

# Verify change
print(book.title)

# Expected Output:
# Nineteen Eighty-Four