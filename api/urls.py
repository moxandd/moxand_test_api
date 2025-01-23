from rest_framework.routers import DefaultRouter
from apps.books import views as books_views

urlpatterns = []

router = DefaultRouter()

router.register('books', books_views.BookViewSet, basename='books')
router.register('authors', books_views.AuthorViewSet, basename='authors')
router.register('genres', books_views.GenreViewSet, basename='genres')

urlpatterns += router.urls