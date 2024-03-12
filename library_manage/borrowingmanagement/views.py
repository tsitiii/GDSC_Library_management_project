from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from bookmanagement.models import Book
from .models import BorrowedBook
from .forms import BorrowBookForm

def borrow_book(request, book_id):
    if request.user.is_authenticated and request.user.is_student:
        num_borrowed_books = BorrowedBook.objects.filter(user=request.user).count()
        if num_borrowed_books < 3:
            book = get_object_or_404(Book, pk=book_id)
            if book.status == 'available':
                BorrowedBook.objects.create(user=request.user, book=book)
                book.status = 'borrowed'
                book.save()
                messages.success(request, 'Book borrowed successfully!')
            else:
                messages.error(request, 'This book is not available for borrowing.')
        else:
            messages.error(request, 'You have already borrowed the maximum number of books.')
    else:
        messages.error(request, 'You are not authorized to borrow books.')

    return redirect('book_list')  # Assuming 'book_list' is the correct URL name
