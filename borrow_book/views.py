import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from borrow_book.forms import BorrowForm
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

@csrf_exempt
def borrow_book(request):
    if request.method == 'POST':
        formData = BorrowForm(request.POST)
        if formData.is_valid:
            book = Book.objects.get(pk=id)
            borrower = request.user
            return_date = formData.get("return_date")
            
            borrow = Borrow.objects.create(book=book, borrower=borrower, borrow_date=datetime.date.today , return_date=return_date)
            borrow.save()
            book.status = False
            book.save()
        
        return HttpResponse(b"CREATED", status= 201)
    
    return HttpResponseNotFound()

def return_book(request, id):
    book = Book.objects.get(pk = id)
    borrowed = Borrow.objects.filter(book=book)
    if request.method == 'POST':
        borrowed.delete()
        book.status = True
        return HttpResponseRedirect(reverse('book_list:show_borrow'))
    
    return HttpResponseNotFound()

def get_book_by_id(request, id):
    book = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', book))

def get_borrow_flutter(request):
    borrow = Borrow.objects.select_related('book').filter(borrower = request.user)
    return HttpResponse(serializers.serialize('json', borrow))

@csrf_exempt
def borrow_flutter(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        book =  Book.objects.get(pk=id)
        borrow = Borrow.objects.create(
            book =book,
            borrower = request.user,
            borrow_date = datetime.date.today,
            return_date= data["return_date"]
        )
        book.status = False

        book.save()
        borrow.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def return_book_flutter(request, id):
    if request.method == "POST":
        borrowed = Borrow.objects.get(pk=id)
        book = borrowed.book
        book.status = True
        borrowed.delete()
        book.save()
    return JsonResponse({"status": "success"}, status=200)
