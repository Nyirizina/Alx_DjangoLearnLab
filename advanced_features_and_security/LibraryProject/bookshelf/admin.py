from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin
# CustomUser is imported above

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
    
    # 1. LIST DISPLAY: What columns show up in the user list
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    
    # 2. FIELDSETS: Controls the layout of the "Edit User" page
    # We copy the default UserAdmin fieldsets and append our custom section
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # 3. ADD FIELDSETS: Controls the layout of the "Add User" page
    # This is used when creating a user via the Admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register the model with the customized admin class
admin.site.register(CustomUser, CustomUserAdmin)