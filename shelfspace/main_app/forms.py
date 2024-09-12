from django import forms
from .models import Book
from .models import Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'genre']

RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING_CHOICES)

    class Meta:
        model = Review
        fields = ['content', 'rating']
