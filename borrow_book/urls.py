from django.urls import path
from .views import show_borrow, get_borrow, borrow_book, return_book

app_name = 'borrow_book'  

urlpatterns = [
    path('', show_borrow, name='show_borrow'),
    path('get-borrow/', get_borrow, name='get_borrow'),
    path('borrow-book/', borrow_book, name = 'borrow_book'),
    path('return-book/', return_book, name='return_book'),
]