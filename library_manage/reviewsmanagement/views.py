from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from bookmanagement.models import Book
from django.db.models import Avg

@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviewsmanagement/review_list.html', {'reviews': reviews})

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('reviewsmanagement:book_detail', book_id=book_id)
    else:
        form = ReviewForm()
    return render(request, 'reviewsmanagement/add_review.html', {'form': form, 'book': book})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviewsmanagement:review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviewsmanagement/edit_review.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('reviewsmanagement:review_list')
    return render(request, 'reviewsmanagement/delete_review.html', {'review': review})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'reviewsmanagement/book_detail.html', {'book': book, 'reviews': reviews, 'average_rating': average_rating})
