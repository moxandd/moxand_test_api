from django.contrib import admin
from apps.books.models import Book, Author, Genre

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id'
    )
   
    readonly_fields = ('id',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'id'
    )
   
    readonly_fields = ('id',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id'
    )
   
    readonly_fields = ('id',)