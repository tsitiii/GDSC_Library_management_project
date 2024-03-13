from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import Book

def register(request):
    msg=None
    if request.method=='POST':
      form=SignUpForm(request.POST) # creating object for the SignUpForm class
      # now we can pass this obj to our template coz we inherited everything we need from the django default forms
      if form.is_valid():
        user=form.save()
        msg='user created'
        return redirect('home')
      else:
          msg='Form is invalid' 
    else:
        form=SignUpForm()

    return render(request, 'account/register.html', {'form': form, 'msg': msg})



def loginview(request):
    form=LoginForm(request.POST)
    msg= None
    if request.method=='POST':
        if form.is_valid():
            Username=form.cleaned_data.get('username')# retrivies the validated data of the username on the above method
            Password=form.cleaned_data.get('password')# retrivies the validated data of the username on the above method
            user=authenticate(username=Username, password=Password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg="Invalid credentials!"
        else:
            msg="Error while validating form!"
    
    return render(request, 'account/login.html',{'form': form, 'msg': msg})

def index(request):
    return render(request,'account/index.html' )


def home(request):
    return render(request, 'account/home.html')

 

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

