from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

class BookView(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.get(id=pk)
            return Response(model_to_dict(book), status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "true", "message": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        try:
            books = Book.objects.all().values()
            return Response({"books": list(books)}, status=status.HTTP_200_OK)
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



