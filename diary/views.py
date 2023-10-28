from django.shortcuts import render
from .models import Diary
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_diary(request):
    diary = Diary.objects.filter(user=request.user)
    booksInDiaryCount = diary.count()

    context = {
        'name': request.user.username,
        'diary': diary,
        'booksInDiaryCount' : booksInDiaryCount,
    }

    return render(request, "diary.html", context)

def get_diary_json(request):
    diaries = Diary.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', diaries))

@csrf_exempt
def add_diary_ajax(request):
    if request.method == 'POST':
        finishDate = request.POST.get("finishDate")
        notes = request.POST.get("notes")
        title = request.POST.get("title")
        user = request.user

        new_diary = Diary(finishDate=finishDate, notes=notes, user=user, title=title)
        new_diary.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()