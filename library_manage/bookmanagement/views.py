from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from account.models import User
from borrowingmanagement.models import BorrowedBook
from django.http import Http404
from django.contrib import messages
from .forms import BookForm

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_admin):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page if not admin or super admin
    return wrapper

@login_required(login_url='login')
@admin_required
def book_list(request):
    books = Book.objects.all()
    us=User.objects.all()
    context={'books':books}
    return render(request, 'bookmanagement/book_list.html', context=context)


@login_required(login_url='login')
@admin_required
def add_book(request):
    if request.method == 'POST':
        # Bind form with POST data and FILES data
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save form data to create a new book object
            messages.success(request, 'Book added successfully.')
            return redirect('bookmanagement:book_list')
        else:
            messages.error(request, 'Form is not valid. Please check your input.')
    else:
        form = BookForm()  # Create a blank form instance if the request method is not POST
    return render(request, 'bookmanagement/AddBook.html', {'form': form})


@login_required
@admin_required
def edit_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('bookid')
        if book_id:
            try:
                book = Book.objects.get(id=book_id)
                book.title = request.POST.get("title")
                book.author = request.POST.get("author")
                book.genre = request.POST.get("genre")
                book.status = request.POST.get("status")
                
                # Handle file inputs separately from request.POST
                if 'file' in request.FILES:
                    book.book_file = request.FILES['file']
                if 'cover' in request.FILES:
                    book.book_cover = request.FILES['cover']
                    
                book.save()
                return redirect('bookmanagement:book_list')
            except Book.DoesNotExist:
                messages.error(request, "Book not found.")
        else:
            messages.error(request, "Invalid request: No book ID provided.")
    else:
        messages.error(request, "Invalid request method.")
    return redirect('bookmanagement:book_list')


    
@login_required(login_url='login')
@admin_required
def editbookview(request):
        book=Book.objects.get(id=request.GET['bookid'])
        print(book)   
        return render(request,'bookmanagement/editbook.html',{'book':book})



@login_required
@admin_required
def delete_book(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return redirect('bookmanagement:book_list')
   



def book_list_view(request):
    books = Book.objects.all()
    search_query = request.GET.get('q')
    genre_filter = request.GET.get('genre')
    author_filter = request.GET.get('author')
    status_filter = request.GET.get('status')

    if search_query:
        books = books.filter(title__icontains=search_query)

    if genre_filter:
        books = books.filter(genre=genre_filter)

    if author_filter:
        books = books.filter(author=author_filter)

    if status_filter:
        books = books.filter(status=status_filter)

    return render(request, 'book_list.html', {'books': books})


def borrowed(request):
    books=BorrowedBook.objects.all()
    print(books)
    return render(request, 'bookmanagement/borrowedbook.html', {'books':books})


@login_required
def banstudent(request):

    if not request.user.is_superuser:
        messages.error(request, 'u are not authorized to ban student.')
    if request.method == 'GET' and 'userid' in request.GET:
        user_id = request.GET['userid']
        try:
            user = User.objects.get(id=user_id)
            user.is_banned = True
            user.save()
            messages.success(request, 'Student banned successfully.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid user ID.')
    else:
        messages.error(request, 'Invalid request.')
    return redirect('bookmanagement:borrowed')

