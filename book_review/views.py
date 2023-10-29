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

@csrf_exempt
def review_list(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'review_list.html', {'book': book, 'reviews': reviews, 'title': book.title, 'id': book.pk})

@csrf_exempt
def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return HttpResponse(b"CREATED", status=201)
    else:
        form = ReviewForm()
    return HttpResponseNotFound()

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
    review = Review.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', review))