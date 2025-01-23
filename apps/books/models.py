from django.db import models
from apps.books.validators import validate_creation_year

# Create your models here.
class Genre(models.Model):
    
    title = models.CharField(blank=False, verbose_name='Жанр', max_length=200)

    class Meta:
        verbose_name = 'Жано'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title

class Author(models.Model):
    
    first_name = models.CharField(blank=False, verbose_name='Имя', max_length=200)
    last_name = models.CharField(blank=False, verbose_name='Фамилия', max_length=200)
    
    surname = models.CharField(blank=True, verbose_name='Отчество', max_length=200)
    birth_date = models.DateTimeField(auto_created=False, auto_now_add=False, null=False, blank=False)


    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Book(models.Model):
    
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Автор')

    creation_year = models.IntegerField(null=True, blank=True, validators=[validate_creation_year])
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Жанр')


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
    


