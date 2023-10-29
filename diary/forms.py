from django.forms import ModelForm, ModelChoiceField
from diary.models import Diary
from book.models import Book

class DiaryForm(ModelForm):
    book = ModelChoiceField(queryset=Book.objects.all(), label="Book")

    class Meta:
        model = Diary
        fields = ["finishDate", "notes", "title"]