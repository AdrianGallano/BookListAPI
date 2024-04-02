from rest_framework import serializers
from .models import Book, Author, Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "no_of_books_published"]

class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=True)
    category = CategorySerializer()
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_price_after_tax')

    def calculate_price_after_tax(self, book:Book):
        return book.price * Decimal(1.1)
    
    class Meta:
        model = Book
        fields = ["title", "price", "inventory", "author", "category", "price_after_tax"]  
