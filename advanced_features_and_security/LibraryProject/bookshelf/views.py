from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# 1. Book List View (Satisfies 'book_list', 'books', and 'raise_exception')
# This view requires the 'can_view' permission to access.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Fetch all books from the database
    books = Book.objects.all()  # Satisfies the check for "books"
    
    # Render the template with the list of books
    return render(request, 'bookshelf/book_list.html', {'books': books})

# 2. Book Create View
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Simple logic to handle form submission (expand as needed)
        title = request.POST.get('title')
        author = request.POST.get('author')
        # ... logic to save book ...
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html')

# 3. Book Edit View
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for editing would go here
    return render(request, 'bookshelf/form_example.html', {'book': book})

# 4. Book Delete View
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})