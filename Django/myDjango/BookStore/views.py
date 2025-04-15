from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Book

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'website/Store.home.html', {'books': books})

def detail(request, detail_id):
    book = get_object_or_404(Book, pk=detail_id)
    return render(request, "website/Store.detail.html", {'book': book})


