from django.urls import path
from .views import *
from forum.views import get_forum_json, add_forum_ajax, get_comment_list, create_comment_ajax, add_comment_ajax, create_post_ajax, delete_forum, get_forum_list
from forum.views import create_comment_ajax, get_comment_list, delete_comment
app_name = 'forum'

urlpatterns = [
    path('', index, name='Forum'),
    path('detail/<int:id>/', forum_post_detail, name="detail"),

    path('get-forum/', get_forum_json, name='get_forum_json'),
    path('create-forum-ajax/', add_forum_ajax, name='add_forum_ajax'),

    
    path('api/ForumHome/', get_forum_list, name="getForumList"),
    path('api/comment/<int:id>/', get_comment_list, name="getCommentList"),
    path('api/addComment/<int:id>/', create_comment_ajax, name="addNewComment"),

    path('detail/<int:id>/add_comment_ajax/', add_comment_ajax, name="getCommentList"),
    path('detail/<int:id>/get_comment_json/', get_comment_json, name="addNewComment"),

    path('api/ForumPage/', get_forum_list, name="getForumList"),
    path('deleteForum/<int:id>/', delete_forum, name="deleteForum"),
    path('api/addForum/', create_post_ajax, name="addNewForum"),

    path('api/comment/<int:id>/', get_comment_list, name="getCommentList"),
    path('api/addComment/<int:id>/', create_comment_ajax, name="addNewComment"),
    path('deleteComment/<int:id>/', delete_comment, name="deleteComment"),
]