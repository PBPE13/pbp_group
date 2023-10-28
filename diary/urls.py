from django.urls import path
from diary.views import show_diary, get_diary_json, add_diary_ajax
app_name = 'diary'

urlpatterns = [
    path('', show_diary, name='show_diary'),
    path('get-diary/', get_diary_json, name='get_diary_json'),
    path('add-book/', add_diary_ajax, name='add_diary_ajax'),
]