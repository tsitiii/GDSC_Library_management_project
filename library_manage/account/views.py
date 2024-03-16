from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from bookmanagement.models import Book

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

def register(request):
    msg=None
    if request.method=='POST':
      form=SignUpForm(request.POST) # creating object for the SignUpForm class
      # now we can pass this obj to our template coz we inherited everything we need from the django default forms
      if form.is_valid():
        # user = form.save(commit=False) # Get the user instance without saving to the database yet
        form.save()
        msg='user created'
        # print("User data:", user.__dict__) #for  debugging purposes
        return redirect('login')
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

            if user is not None and user.is_student:
                login(request, user)
                return redirect('home')
            
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('bookmanagement:book_list')
            
            if user is not None and user.is_super_admin or user.is_superuser:
                login(request, user)
                return redirect('admin')
            else:
                msg="Invalid credentials!"
        else:
            msg="Error while validating form!"
    
    return render(request, 'account/login.html',{'form': form, 'msg': msg})



def logoutform(request):
    logout(request)
    return render(request, 'account/logout.html')


@login_required(login_url='login')
def admin(request):
    return redirect('admin/')


def index(request):
    return render(request,'account/index.html' )


def home(request):
    books = Book.objects.all()
    return render(request, 'account/home.html', {"books" : books})

 



