from django.shortcuts import render

# Create your views here.
from apps.books.mixins import BookViewSetMixin, AuthorViewSetMixin, GenreViewSetMixin
from apps.books.models import Book, Author, Genre
from apps.books.serializers import BookSerializer, AuthorSerializer, GenreSerializer


# Create your views here.

class BookViewSet(BookViewSetMixin):
    def get_serializer_class(self):
        return BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class AuthorViewSet(AuthorViewSetMixin):
    def get_serializer_class(self):
        return AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()
    

class GenreViewSet(GenreViewSetMixin):
    def get_serializer_class(self):
        return GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()
    