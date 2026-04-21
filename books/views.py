from django.shortcuts import render
from django.views import View

from books.models import Book


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'booklist.html', {'kitoblar': books})

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        return render(request, 'bookdetail.html', {'kitob': book})