from django.urls import path
from book_review.views import review_list, add_review, edit_review, delete_review, get_review_json
from book_review.views import add_review_flutter


urlpatterns = [
    path('', review_list, name='review_list'),
    path('add_review/', add_review, name='add_review'),
    path('edit_review/<int:review_id>/', edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', delete_review, name='delete_review'),
    path('get-review-json/', get_review_json, name='get_review_json'),
    path('add-review-flutter/', add_review_flutter, name='add_review_flutter'),
]
