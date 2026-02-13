from .models import Author, Book
from rest_framework import serializers

# Serializers define the API representation.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', ]
# Custom validation to ensure publication year is not in the future
    def validate(self, data):
        if data['publication_year'] > 2026:
            raise serializers.ValidationError("Publication year cannot be in the future.")

# Serializer for the Author model, including a nested list of their books
class AuthorSerializer(serializers.ModelSerializer):
    Books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'Books']

