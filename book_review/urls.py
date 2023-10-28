from django.urls import path
from book_review.views import review_list, add_review, edit_review, delete_review


urlpatterns = [
    path('book/<int:book_id>/book_reviews/', review_list, name='review_list'),
    path('book/<int:book_id>/book_reviews/add/', add_review, name='add_review'),
    path('book_reviews/<int:review_id>/edit/', edit_review, name='edit_review'),
    path('book_reviews/<int:review_id>/delete/', delete_review, name='delete_review'),
]
