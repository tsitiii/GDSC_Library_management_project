from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.loginview, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('books/', views.book_list_view, name='book_list'),
    path('search/', views.search, name = 'search-books')
]

