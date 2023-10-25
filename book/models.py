from django.db import models

# Create your models here.
class Book(models.Model):
    bookID = models.IntegerField(null= True, blank= True) 
    title= models.TextField(null= True, blank= True) 
    authors= models.TextField(null= True, blank= True) 
    average_rating= models.FloatField(null= True, blank= True) 
    isbn = models.TextField(null= True, blank= True)
    isbn13 = models.IntegerField(null= True, blank= True)
    language_code= models.TextField(null= True, blank= True)
    num_pages = models.IntegerField(null= True, blank= True)
    ratings_count= models.IntegerField(null= True, blank= True)
    text_review_count = models.IntegerField(null= True, blank= True)
    publication_date= models.TextField(null= True, blank= True)
    publisher = models.TextField(null= True, blank= True)