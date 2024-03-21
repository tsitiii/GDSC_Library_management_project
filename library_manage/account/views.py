from datetime import datetime
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from borrowingmanagement.models import BorrowedBook
from bookmanagement.models import Book
from .models import User



def register(request):
    msg=None
    if request.method=='POST':
      form=SignUpForm(request.POST) 
      # now we can pass this obj to our template coz we inherited everything we need from the django default forms
      if form.is_valid():
        form.save()
        msg='user created'
        return redirect('login')
      else:
          msg='Form is invalid' 
    else:
        form=SignUpForm()
    context={'Form': form, 'msg': msg}
    return render(request, 'account/register.html', context=context)

def terms_and_conditions(request):
    return render(request, 'account/terms_and_conditions.html')


def loginview(request):
    form=LoginForm()
    msg= None
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid(): #checking if the form we defined in the forms.py have no error
            Username=form.cleaned_data.get('username')# retrivies the validated data of the username that we defined in our forms.py
            Password=form.cleaned_data.get('password')# retrivies the validated data of password in our forms.py
      
            user=authenticate(username=Username, password=Password)

            if user is not None and user.is_student:
                login(request, user)
                # flag = True
                return redirect('home')
            
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('bookmanagement:book_list')
            
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin')
            else:
                msg="Invalid credentials!"
        else:
            msg="Error while validating form!"
    context={'form': form, 'msg': msg}
    return render(request, 'account/login.html',context=context)

def logoutform(request):
    logout(request)
    return render(request, 'account/logout.html')

@login_required(login_url='login')
def admin(request):
    return redirect('admin/')
def home(request):
    now = datetime.now()
    return render(request, 'account/home.html', {'now': now})

def index(request):
    return render(request,'account/index.html' )

@login_required(login_url='login')
def home(request):
    books = Book.objects.all()
    return render(request, 'account/home.html', {"books" : books})

@login_required
def profile(request):
    user = request.user
    borrowed = BorrowedBook.objects.filter(user = user)
    books = []
    for book in borrowed:
        books.append(book.book)


    return render(request, 'account/myaccount.html', {"user" : user, "books" : books})




def search(request):
    if request.method == "POST": 
        searched = request.POST["search"]

        books = Book.objects.filter(title__contains = searched)
        return render(request, 'account/search.html', {"searched" : searched, "books" : books, "by" : "title"})
    
    return render(request, 'account/search.html', {})

def search_author(request):
    if request.method == "POST": 
        searched = request.POST["search_author"]

        books = Book.objects.filter(author__contains = searched)
        return render(request, 'account/search.html', {"searched" : searched, "books" : books, "by" : "author"})
    
    return render(request, 'account/search.html', {})


def filtered_books(request, genre):
    if genre == 'all':
        books = Book.objects.all()
    else:
        books = Book.objects.filter(genre = genre)

    return render(request,'account/home.html', {"books" : books} )

def status_filter(request):

    books = Book.objects.filter(status = "available")

    return render(request,'account/home.html', {"books" : books} )
 



