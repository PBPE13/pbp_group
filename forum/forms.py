from django.db import models
from django import forms
from .models import *
from django.contrib.auth.decorators import login_required

class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['topic', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']