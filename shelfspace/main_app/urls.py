from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('books/', views.books_index, name='books_index'),  # List all books
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # Book detail view
    path('books/new/', views.book_create, name='book_create'),  # Add Book Form
    path('books/<int:book_id>/edit/', views.book_update, name='book_update'),  # Update Book
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),  # Delete Book
]