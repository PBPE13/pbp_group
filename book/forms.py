from django import forms
from book.models import Book

class BookForm(forms.Form):
    class meta:
        model = Book
    title= forms.CharField(label='Judul', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'title'})) 
    authors= forms.CharField(label='Penulis', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'authors'})) 
    publisher = forms.CharField(label='Penerbit', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'publisher'}))