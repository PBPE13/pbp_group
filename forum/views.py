from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from requests import Response
from book.models import Book
from forum.models import Comment, ForumPost
from .forms import ForumForm, CommentForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

    
# Create your views here.
@csrf_exempt
def get_forum_list(request):
    list_post = ForumPost.objects.all().order_by('-date')
    user = request.user.username
    ret = [user]
    for posts in list_post:
        temp = {
            "pk": posts.pk,
            "user": posts.user.username,
            "topic": posts.topic,
            "description":posts.description,
            "title":posts.title,
            "date":posts.date.date(), 
        }
        ret.append(temp)

    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')


def index(request):
    forumPost = ForumPost.objects.all().order_by('-date')
    books = Book.objects.all().order_by('title')
    response = {'forumPost': forumPost , 'books':books}
    return render(request, 'forumPage.html', response)

@csrf_exempt
def get_comment_list(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost).order_by('-date')
    user = request.user.username
    ret = [user]
    for comment in comments:
        temp = {
            "pk": comment.pk,
            "user": comment.user,
            "parentForum": comment.parentForum,
            "description": comment.description,
            "date": comment.date.date(),
        }
        ret.append(temp)
    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')


def get_comment_json(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost).order_by('-date')
    return HttpResponse(serializers.serialize('json', comments))

def forum_post_detail(request,id):
    forumPost = ForumPost.objects.get(pk=id)
    commentForm = CommentForm()
    return render(request, 'forumDetail.html', {'forumPost':forumPost, 'commentForm':commentForm})


@login_required(login_url='/login')
@csrf_exempt
def create_post_ajax(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        description = request.POST.get("description")
        title=request.POST.get("title")

        new_forum = ForumPost.objects.create(
            topic=topic,
            description=description,
            date=datetime.date.today(),
            user=request.user,
            title=title
        )
        result = {
            'pk':new_forum.pk,
            'user':new_forum.user.username,
            'topic':new_forum.topic,
            'description':new_forum.description,
            'date':new_forum.date.date(),
            'title':new_forum.title  
        }
        return JsonResponse(result, status=200)
    return render(request, "forumPage.html")


@login_required(login_url='/login')
@csrf_exempt
def delete_forum(request, id):
    if request.method == "DELETE":
        forum = get_object_or_404(ForumPost, id=id)
        forum.delete()
    return HttpResponse(status=202)

@login_required(login_url='/authentications/login')
@csrf_exempt
def create_comment_ajax(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    if request.method == "POST":
        description = request.POST.get("description")
        title = request.POST.get('title')
        new_comment = Comment.objects.create(
            parentForum=forumPost,
            description=description,
            date=datetime.date.today(),
            user=request.user,
        )
        result = {
            'pk':new_comment.pk,
            'user':new_comment.user.username,
            'description':new_comment.description,
            'date':new_comment.date.date(),
        }
        return JsonResponse(result, status=200)
    return render(request, "forumPage.html")

@csrf_exempt
def get_comment_list(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost).order_by('-date')
    user = request.user.username
    ret = [user]
    for comment in comments:
        temp = {
            "pk": comment.pk,
            "user": comment.user,
            "parentForum": comment.parentForum,
            "description": comment.description,
            "date": comment.date.date(),
        }
        ret.append(temp)
    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')

@login_required(login_url='/login')
@csrf_exempt
def delete_comment(request, id):
    if request.method == "DELETE":
        comment = get_object_or_404(Comment, id=id)
        comment.delete()
    return HttpResponse(status=202)

@csrf_exempt
def flutter_forum(request):
    list_post = ForumPost.objects.all().order_by('-date')
    ret = []
    for posts in list_post:
        temp = {
            "pk": posts.pk,
            "user": posts.user.username,
            "topic": posts.topic,
            "description":posts.description,
            "date":posts.date.date(),
            "title":posts.title
        }
        ret.append(temp)

    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def flutter_comment(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost).order_by('-date')
    ret = []
    for comment in comments:
        temp = {
            "pk": comment.pk,
            "user": comment.user,
            "parentForum": comment.parentForum.pk,
            "description": comment.description,
            "date": comment.date.date(),
        }
        ret.append(temp)
    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')
    

@login_required(login_url='/authentication/login')
@csrf_exempt
def flutter_add_forum(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        title = request.POST['title']
        description = request.POST['description']
        ForumPost.objects.create(
            topic=topic,
            description=description,
            date=datetime.date.today(),
            user=request.user,
            title=title
        )
        print("success")
        return JsonResponse({'status': 'success'})

@login_required(login_url='/authentications/login')
@csrf_exempt
def flutter_add_comment(request, id):
    if request.method == 'POST':
        try:
            forumPost = ForumPost.objects.get(pk=id)
            description = request.POST['description']

            Comment.objects.create(
                parentForum=forumPost,
                description=description,
                date=datetime.date.today(),
                user=request.user,
            )
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status':'failed'})
