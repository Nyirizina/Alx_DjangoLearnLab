from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right sidebar
    list_filter = ('publication_year', 'author')

    # Add a search bar at the top
    search_fields = ('title', 'author')





class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields' : ('date_of_birth', 'profile_photo')}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields' : ('date_of_birth', 'profile_photo')}),)
admin.site.register(CustomUser, CustomUserAdmin)