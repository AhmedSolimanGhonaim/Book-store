from django.shortcuts import render

# Create your views here.
from books.models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookListApiView(generics.ListAPIView): # read only
    serializer_class = BookSerializer
    queryset = Book.objects.all()
