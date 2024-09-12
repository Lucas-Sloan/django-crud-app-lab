from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.id})
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(max_length=500)
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} - {self.rating}/5"