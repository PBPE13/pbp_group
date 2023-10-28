from django.urls import path
from .views import show_borrow

app_name = 'borrow_book'  

urlpatterns = [
    path('show-borrow', show_borrow, name='show_borrow'),
]