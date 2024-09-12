from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review
from .forms import BookForm, ReviewForm

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

def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book = book
            new_review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()
    
    return render(request, 'books/add_review.html', {'form': form, 'book': book})

def update_review(request, book_id, review_id):
    book = get_object_or_404(Book, id=book_id)
    review = get_object_or_404(Review, id=review_id, book=book)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'reviews/review_form.html', {'form': form, 'book': book, 'review': review})

def delete_review(request, book_id, review_id):
    book = get_object_or_404(Book, id=book_id)
    review = get_object_or_404(Review, id=review_id, book=book)

    if request.method == 'POST':
        review.delete()
        return redirect('book_detail', book_id=book.id)
    
    return render(request, 'reviews/review_confirm_delete.html', {'book': book, 'review': review})