from django.urls import path
from . import views

from borrowingmanagement.views import borrow_book
from bookmanagement.urls import book_list

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/',views.logoutform, name='logout'),
    path('login/',views.loginview, name='login'),
    path('register', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('admin', views.admin, name='admin'),
    path('search/', views.search, name = 'search-books'),    
    path('search_author/', views.search_author, name = 'search-author'),    
    path('filtered_books/<str:genre>/', views.filtered_books, name='filtered_books'),
    path('profile/', views.profile, name = "profile"), 
    path('borrow/',borrow_book, name = 'borrow' ),
    path('books/',book_list, name = 'books' )
   
]


