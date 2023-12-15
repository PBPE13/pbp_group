from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    review_date = models.DateTimeField(auto_now_add=True)