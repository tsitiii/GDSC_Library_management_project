from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login


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

  