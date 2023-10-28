from django.urls import path
from book.views import get_books, show_books

app_name = 'book'

urlpatterns = [
    path('api/book/', get_books, name='get_books'),
    path('', show_books, name='show_books'),
]