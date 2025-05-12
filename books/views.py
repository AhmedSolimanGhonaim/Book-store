from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from .models import Book


class BookListView(ListView):
    model = Book 
    template_name = 'books/book_list.html' 


class AboutView(TemplateView):
    template_name = 'books/about.html'