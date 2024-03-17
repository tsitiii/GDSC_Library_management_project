from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from bookmanagement.models import Book
from .models import BorrowedBook
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required(login_url='login')
def borrow_book(request, book_id):
    if request.user.is_authenticated and request.user.is_student and not request.user.is_banned:
        num_borrowed_books = BorrowedBook.objects.filter(user=request.user).count()
        if num_borrowed_books < 3:
            book = get_object_or_404(Book, pk=book_id)
            if book.status == 'available':
                BorrowedBook.objects.create(user=request.user, book=book)
                book.status = 'borrowed'
                book.save()
                messages.success(request, 'Book borrowed successfully!')
                return redirect('home')
            else:
                messages.success(request, 'Book is already borrowed')
                return redirect('borrowingmanagement:profile_view')
        else:
            messages.success(request, 'You already borrowed 3 books.')
            return redirect('borrowingmanagement:profile_view')
    elif request.user.is_authenticated and request.user.is_banned:
        messages.success(request, 'you are banned from borrowing books')
        return redirect('borrowingmanagement:profile_view')

    elif not(request.user.is_authenticated):
       messages.success(request, 'You are not auhtorized to borrow books. Register and u will get access to it!')
       return redirect('borrowingmanagement:profile_view')

    return redirect('account:home') 


def profile_view(request):
        user = request.user
        borrowed_books = user.borrowedbook_set.all()
     
        return  render(request, 'borrowingmanagement/borrowbook.html', {'borrowed_books':borrowed_books})
    
def return_book(request, book_id):
    borrowed_book=get_object_or_404(BorrowedBook, book_id=book_id, user=request.user)
    borrowed_book.book.status='available'
    borrowed_book.return_date=date.today()
    borrowed_book.save()
    borrowed_book.user.books_borrowed-=1
    borrowed_book.save()
    return redirect('profile')
