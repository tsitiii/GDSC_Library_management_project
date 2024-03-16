from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from account.models import User
from borrowingmanagement.models import BorrowedBook
from django.http import Http404
from django.contrib import messages

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # Redirect to login page if not admin or super admin
    return wrapper

# NO Login Required;
def book_list(request):
    books = Book.objects.all()
    us=User.objects.all()
    context={'books':books, 'user':us}
    return render(request, 'bookmanagement/book_list.html', context=context)


@login_required(login_url='login')
@admin_required
def add_book(request):
    if request.method == 'POST':
        t = request.POST["title"]
        a = request.POST["author"]
        g = request.POST["genre"]
        c = request.POST["cover"]
        f = request.POST["file"]
        r=request.POST['rating']
        
        book = Book()
        book.title = t
        book.author = a
        book.genre = g
        book.book_cover = c
        book.book_file = f
        book.ratings=r
        book.save()
        
        return redirect('bookmanagement:book_list')

    return render(request, 'bookmanagement/AddBook.html')


@login_required(login_url='login')
@admin_required
def edit_book(request):
    if request.method=='POST':
        t= request.POST["title"]
        a= request.POST["author"]
        g = request.POST["genre"]
        s=request.POST["status"]
        f=request.POST["File"]
        c=request.POST['cover']

        book= Book.objects.get(id=request.POST['bookid'])
        book.title=t
        book.author=a
        book.genre = g
        book.status=s
        book.book_file=f
        book.book_cover=c
        book.save()
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
    if not request.user.is_super_admin:
        raise Http404()  # Only super admins can access this view

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

