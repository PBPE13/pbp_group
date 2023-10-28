from django.forms import ModelForm, ModelChoiceField
from main.models import Diary
from book.models import Book

class BookForm(ModelForm):
    book = ModelChoiceField(queryset=Book.objects.all(), label="Book")

    class Meta:
        model = Diary
        fields = ["finishDate", "notes", "title"]