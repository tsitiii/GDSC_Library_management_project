from django.urls import path
from .views import book_list, add_book, edit_book, delete_book, book_list_view

app_name = 'bookmanagement'

urlpatterns = [
    path('booklist', book_list, name='book_list'),
    path('AddBook', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
    path('books/', book_list_view, name='book_list')
]
