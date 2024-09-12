from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def home(request):
    return render(request, 'home.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_index')
    else:
        form = BookForm()

    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'book': book})

def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_index')
    return render(request, 'books/book_confirm_delete.html', {'book': book})