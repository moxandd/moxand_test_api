from rest_framework.test import APITestCase
from rest_framework import status
from apps.books.models import Book, Author, Genre
from django.urls import reverse

class BookAPITests(APITestCase):
    def setUp(self):
        # Создание автора и жанра для тестирования
        self.author = Author.objects.create(first_name="J.K.", last_name="Rowling", birth_date="1965-07-31")
        self.genre = Genre.objects.create(title="Fantasy")

        # Создание книги для тестирования
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            author=self.author,
            genre=self.genre,
            creation_year=1997
        )
        self.url = reverse('books-list')  # Сгенерированный URL для списка книг (из URL с basename='books')

    def test_create_book(self):
        """Тест создания новой книги."""
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "author": self.author.id,
            "genre": self.genre.id,
            "creation_year": 1998
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Проверяем, что книга добавлена
        self.assertEqual(response.data['title'], data['title'])

    def test_get_books(self):
        """Тест получения списка книг."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]), 5)  # Проверяем, 
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_get_book_detail(self):
        """Тест получения подробностей книги по ID."""
        url = reverse('books-detail', args=[self.book.id])  # Используем имя URL-шаблона для детали книги
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)