from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right sidebar
    list_filter = ('publication_year', 'author')

    # Add a search bar at the top
    search_fields = ('title', 'author')