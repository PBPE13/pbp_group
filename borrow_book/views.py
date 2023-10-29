from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from borrow_book.models import Borrow
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
def show_borrow(request):
    user = request.user
    borrows = Borrow.objects.filter(borrower=request.user)
    context = {
        'borrower': user,
        'borrows' : borrows,
        'date' : datetime.date.today,
        'jumlah_dipinjam' : borrows.count(),
    }
    return render(request, 'borrow.html', context)

def get_borrow(request):
    borrows = Borrow.objects.filter(borrower=request.user)
    return HttpResponse(serializers.serialize('json', borrows))


def borrow_book(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk =id)
        borrower = request.user
        return_date = request.POST.get("return_date")

        borrow = Borrow(book= book, borrower = borrower, borrow_date = datetime.date.today , return_date = return_date )
        borrow.save()

        return HttpResponse(status= 201)
    
    return HttpResponseNotFound()

def return_book(request, id):
    if request.method == 'POST':
        borrow = get_object_or_404(Borrow, pk=id)
        book = borrow.book
        Borrow.objects.get(pk= id).delete()
        return HttpResponse(b"DELETED", status=201)
    
    return HttpResponseNotFound()