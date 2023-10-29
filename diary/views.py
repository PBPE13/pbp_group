from django.shortcuts import render
from django.urls import reverse
from .models import Diary
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import DiaryEditForm

# Create your views here.
@login_required(login_url='main:login')
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

def edit_diary(request, id):
    diary = Diary.objects.get(pk=id)

    form = DiaryEditForm(request.POST or None, instance=diary)
    if form.is_valid() and request.method == "POST":

        form.save()
        return HttpResponseRedirect(reverse('diary:show_diary'))

    context = {'form': form}
    return render(request, "edit_diary.html", context)

def delete_diary(request, id):
    diary = Diary.objects.get(pk =id)
    diary.delete()
    return HttpResponseRedirect(reverse('diary:show_diary'))