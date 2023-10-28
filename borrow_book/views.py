from django.shortcuts import render
from borrow_book.models import Borrow
from main.models import Book
import datetime

# Create your views here.
def show_borrow(request):
    user = request.user
    borrows = Borrow.objects.filter(user=request.user)
    context = {
        'books' : borrows,
    }
    return render(request, 'borrow.html', context)