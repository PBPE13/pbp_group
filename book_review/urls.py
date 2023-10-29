from django.urls import path
from book_review.views import review_list, add_review, edit_review, delete_review


urlpatterns = [
    path('<int:book_id>/', review_list, name='review_list'),
    path('<int:book_id>/add_review/', add_review, name='add_review'),
    path('<int:book_id>/edit_review/<int:review_id>/', edit_review, name='edit_review'),
    path('<int:book_id>/delete_review/<int:review_id>/', delete_review, name='delete_review'),
]
