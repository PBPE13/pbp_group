from django.urls import path
from .views import show_borrow, get_borrow, borrow_book, return_book, borrow_flutter, get_borrow_flutter, return_book_flutter, get_book_by_id

app_name = 'borrow_book'  

urlpatterns = [
    path('', show_borrow, name='show_borrow'),
    path('get-borrow/', get_borrow, name='get_borrow'),
    path('borrow-book/', borrow_book, name = 'borrow_book'),
    path('return-book/', return_book, name='return_book'),
    path('get-book-by-id/<int:id>/', get_book_by_id, name="get_book_by_id"),
    path('borrow-flutter/',borrow_flutter,name="borrow_flutter" ),
    path('get-borrow-flutter/', get_borrow_flutter, name= "get_borrow_flutter"),
    path('return-book-flutter/', return_book_flutter, name="return_book_flutter")
]