from django.db import models
from django import forms
from .models import *
from django.contrib.auth.decorators import login_required
from book.models import Book


class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['topic','description']
    



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        widgets = {"description": forms.Textarea(attrs={"class": "form-control"}),
        }