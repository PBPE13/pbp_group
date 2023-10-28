from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from book.models import Book
from book.forms import BookForm
from main.models import Profile
from django.views.decorators.csrf import csrf_exempt

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type= "application/json")

def show_books(request):
    form = BookForm(request.POST or None)
    book = Book.objects.all()
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user)
        context = {
            'book' : book,
            'profile' : profile,
            'form' : form,
        }
    else:
        context = {
            'book' : book,
        }
    return render(request, 'book.html', context)