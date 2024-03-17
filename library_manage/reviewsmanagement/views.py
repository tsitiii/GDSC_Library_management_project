from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from bookmanagement.models import Book
from django.db.models import Avg

#@login_required
def book_detail(request, book_title):
    book = get_object_or_404(Book, title=book_title)
    reviews = Review.objects.filter(book=book)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('reviewsmanagement:book_detail', book_title=book_title)
    else:
        form = ReviewForm()

    return render(request, 'reviewsmanagement/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form
    })

#@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviewsmanagement:book_detail', book_title=review.book.title)
    else:
        form = ReviewForm(instance=review)
    # Get the book associated with the review
    book = review.book
    
    return render(request, 'reviewsmanagement/book_detail.html', {'book': book, 'form': form})

#@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('reviewsmanagement:book_detail', book_title=review.book.title)
    # Get the book associated with the review
    book = review.book
    return render(request, 'reviewsmanagement/delete_review.html', {'review': review, 'book': book})
