from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.core import serializers
from book.models import Book
from book_review.models import Review
from .forms import ReviewForm
import json

@csrf_exempt
def review_list(request):
    return render(request, 'review_list.html')

@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        book = request.POST.get("book")
        rating = request.POST.get("rating")
        content = request.POST.get("content")
        user = request.user

        new_review = Review(book = book, rating=rating, content=content, user=user)
       
        new_review.save()
        return HttpResponse(b"CREATED", status=201)
 

@csrf_exempt
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'POST':
        try:
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "Review updated successfully"}, status=200)
        except Review.DoesNotExist:
            return JsonResponse({"error": "Review not found"}, status=404)
    else:
        form = ReviewForm(instance=review)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect(reverse('book_review:review_list'))
    return HttpResponseNotFound()

def get_review_json(request):
    review = Review.objects.all()
    return HttpResponse(serializers.serialize('json', review))

@csrf_exempt
def add_review_flutter(request):
    if request.method == 'POST':
        input = json.loads(request.body)
        
        new_review = Review.objects.create(
            user = request.user,
            book = input["book"],
            rating = input["rating"],
            content = input["content"],
        )
        new_review.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_review_flutter(request, id):
    if request.method == "POST":
        review_item = Review.objects.get(pk=id)
        review_item.delete()

        return JsonResponse({"status": "success", "message": "Success!"}, status=200)

    return JsonResponse({"status": "failed", "message": "Failed!"}, status=400)
        