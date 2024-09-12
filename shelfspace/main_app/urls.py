from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('books/', views.books_index, name='books_index'),  # List all books
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # Book detail view
    path('books/new/', views.book_create, name='book_create'),  # Add Book Form
    path('books/<int:book_id>/edit/', views.book_update, name='book_update'),  # Update Book
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),  # Delete Book
    path('books/<int:book_id>/reviews/add/', views.add_review, name='add_review'), # Add Review Form
    path('books/<int:book_id>/reviews/<int:review_id>/edit/', views.update_review, name='update_review'),  # Update review
    path('books/<int:book_id>/reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),  # Delete review
]