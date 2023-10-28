from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.
class ForumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.TextField(null= True, blank= True) 
    topic = models.CharField(max_length=140, default="none")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.topic

    def snippets(self):
        if len(self.description) <= 1000:
            return self.description
        else:
            return self.description[:1000] + "..."
        
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    parentForum = models.ForeignKey(ForumPost, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    date= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description[:20]
