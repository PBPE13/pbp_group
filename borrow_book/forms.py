from django.forms import ModelForm
from borrow_book.models import Borrow

class BorrowForm(ModelForm):
    class meta:
        model = Borrow
        fields = ["return_date"]
