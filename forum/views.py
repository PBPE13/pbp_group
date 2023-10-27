from django.shortcuts import render, redirect, get_object_or_404
from requests import Response
from forum.models import ForumPost
from .forms import *
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
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
            "date":posts.date.date(), 
        }
        ret.append(temp)

    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')

def get_forum_json(request):
    forum_item = ForumPost.objects.all()
    return HttpResponse(serializers.serialize('json', forum_item))

def index(request):
    forumPost = ForumPost.objects.all().order_by('-date')
    response = {'forumPost': forumPost}
    return render(request, 'forumPage.html', response)

@csrf_exempt
@login_required(login_url='/login')
def add_forum_ajax(request):
   if request.method == 'POST':
      topic = request.POST.get("topic")
      description = request.POST.get("description")
      user = request.user
      new_forum = ForumPost(topic=topic, description=description, user=user)
      new_forum.save()

      return HttpResponse(b"CREATED", status=201)
   return HttpResponseNotFound()

@login_required(login_url='/login')
@csrf_exempt
def create_comment_ajax(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    if request.method == "POST":
        description = request.POST.get("description")
        role = request.POST.get('role')
        new_comment = Comment.objects.create(
            parentForum=forumPost,
            description=description,
            date=datetime.date.today(),
            user=request.user,
        )
        result = {
            'pk':new_comment.pk,
            'author':new_comment.user.username,
            'description':new_comment.description,
            'date_created':new_comment.date.date(),
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
            "author": comment.user,
            "parentForum": comment.parentForum,
            "description": comment.description,
            "date_created": comment.date.date(),
        }
        ret.append(temp)
    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')


def get_comment_json(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost).order_by('-date')
    return HttpResponse(serializers.serialize('json', comments))

@csrf_exempt
@login_required(login_url='/login')
def add_comment_ajax(request, id):
   forumPost = ForumPost.objects.get(pk=id)
   if request.method == 'POST':  
      description = request.POST.get("description")
      new_comment = Comment(
            parentForum=forumPost,
            description=description,
            date=datetime.date.today(),
            user=request.user,
        )
      new_comment.save()

      return HttpResponse(b"CREATED", status=201)
   return HttpResponseNotFound()

def forum_post_detail(request,id):
    forumPost = ForumPost.objects.get(pk=id)
    return render(request, 'forumDetail.html', {'forumPost':forumPost})


