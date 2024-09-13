from django import forms
from .models import Book, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

