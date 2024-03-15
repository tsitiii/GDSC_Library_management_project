from django.urls import path
from .views import book_list, add_book, edit_book, delete_book

app_name = 'bookmanagement'

urlpatterns = [
    path('booklist/', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
]
