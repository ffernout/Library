from django.shortcuts import render
from .models import Book

def all_category_book(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'tags/all_category_book.html', {'books': books})

def children_books(request):
    books = Book.objects.filter(category='Книги для детей')
    return render(request, 'tags/children_books.html', {'books': books})

def teen_books(request):
    books = Book.objects.filter(category='Книги для подростков')
    return render(request, 'tags/teen_books.html', {'books': books})