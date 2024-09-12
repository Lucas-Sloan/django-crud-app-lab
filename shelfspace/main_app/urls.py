from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('books/', views.books_index, name='books_index'),  # List all books
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # Book detail view
]