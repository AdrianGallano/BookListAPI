from .models import Book, Category, Author
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer
from django.forms.models import model_to_dict
import json

class BookView(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.get(id=pk)
            serialized_book = BookSerializer(book, context={"request":request})
            return Response(serialized_book.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "true", "message": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        try:
            books = Book.objects.select_related("category").all()
            serialized_books = BookSerializer(books, many=True, context={"request":request})

            return Response(serialized_books.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "true", "message": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        payload = json.loads(request.body)

        title = payload.get("title")
        author = payload.get("author")
        price = payload.get("price")
        try:
            book = Book.objects.create(title=title, author=author, price=price)

            inventory = payload.get("inventory")
            if inventory:
                book.inventory = inventory

            book.save()
            return Response({"success": "true", "message": "Created Successfuly"}, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            return Response({"error": "true", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CategoryView(ViewSet):
    def list(self, request):
        categories = Category.objects.all()
        serialized_category = CategorySerializer(categories, many=True)

        return Response(serialized_category.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        serialized_category = CategorySerializer(categories)
        
        return Response(serialized_category.data, status=status.HTTP_200_OK)

class AuthorView(ViewSet):
    def list(self, request):
        authors = Author.objects.all()
        serialized_authors = AuthorSerializer(authors, many=True)
        return Response(serialized_authors.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        author = Author.objects.get(pk=pk)
        serialized_author = AuthorSerializer(author)
        
        return Response(serialized_author.data, status=status.HTTP_200_OK)
