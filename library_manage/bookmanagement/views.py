from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

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
    return render(request, 'bookmanagement/book_list.html', {'books': books})


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

# @login_required
# @admin_required
# def edit_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('bookmanagement:booklist')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'bookmanagement/editbook.html', {'form': form})


@login_required(login_url='login')
@admin_required
def edit_book(request):
    if request.method=='POST':
        t= request.POST["title"]
        a= request.POST["author"]
        g = request.POST["genre"]
        s=request.POST["status"]

        book= Book.objects.get(id=request.POST['bookid'])
        book.title=t
        book.author=a
        book.genre = g
        book.status=s
        book.save()
        return redirect('bookmanagement:booklist')
def editbookview(request):
        # book=Book.objects.get(id=request.GET['bookid'])
        # print(book)   
        return render(request,'bookmanagement/editbook.html')



@login_required
@admin_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('bookmanagement:book_list')
    return render(request, 'bookmanagement/deletebook.html', {'book': book})



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