from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})