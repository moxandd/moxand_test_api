# Django API Project

## Описание

## Этот проект — API для управления книгами, авторами и жанрами, разработанный с использованием Django и Django REST Framework (DRF). API предоставляет возможность создавать, читать, обновлять и удалять книги, авторов и жанры.

Структура проекта
Books: Управление книгами.
Authors: Управление авторами книг.
Genres: Управление жанрами книг.

## Требования

    asgiref==3.8.1
    Django==5.1.5
    django-rest-framework==0.1.0
    djangorestframework==3.15.2
    sqlparse==0.5.3
    tzdata==2025.1

# Установка

## 1. Клонировать репозиторий

git clone https://github.com/yourusername/your-django-api-project.git
cd moxand_test_api

## 2. Создание виртуального окружения Linux/Windows

python -m venv venv
source venv/bin/activate  
venv\Scripts\activate

## 3. Установка зависимостей

pip install -r requirements.txt

## 4. Настройка базы данных и создание admin ()

python manage.py migrate
python manage.py createsuperuser -> username/password

## 5. Запуск серверa разработки

python manage.py runserver

По умолчанию сервер будет доступен по адресу: http://127.0.0.1:8000/api
API Endpoints
Books

    GET /api/books/ — Получить список всех книг.
    POST /api/books/ — Создать новую книгу.
    GET /api/books/{id}/ — Получить детали книги по ID.
    PUT /api/books/{id}/ — Обновить данные книги.
    DELETE /api/books/{id}/ — Удалить книгу.

Authors

    GET /api/authors/ — Получить список всех авторов.
    POST /api/authors/ — Создать нового автора.
    GET /api/authors/{id}/ — Получить детали автора по ID.
    PUT /api/authors/{id}/ — Обновить данные автора.
    DELETE /api/authors/{id}/ — Удалить автора.

Genres

    GET /api/genres/ — Получить список всех жанров.
    POST /api/genres/ — Создать новый жанр.
    GET /api/genres/{id}/ — Получить детали жанра по ID.
    PUT /api/genres/{id}/ — Обновить данные жанра.
    DELETE /api/genres/{id}/ — Удалить жанр.

Пример запроса (GET /api/books/)

Пример запроса для получения списка книг:

curl -X GET http://127.0.0.1:8000/api/books/

Пример ответа:

{
"next": null,
"previous": null,
"data": [
{
"id": 1,
"title": "Harry Potter and the Philosopher's Stone",
"author": 1,
"genre": 1,
"creation_year": 1997
}
]
}

Создание книги

Пример запроса для создания книги:

curl -X POST http://127.0.0.1:8000/api/books/ \
-H "Content-Type: application/json" \
-d '{
"title": "Harry Potter and the Chamber of Secrets",
"author": 1,
"genre": 1,
"creation_year": 1998
}'

## Тестирование

1. Запуск тестов

Для запуска тестов используйте команду:

python manage.py test apps.books.tests.test_books_api
