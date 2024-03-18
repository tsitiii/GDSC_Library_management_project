from django.urls import path
from .views import *

app_name = 'bookmanagement'

urlpatterns = [
    path('booklist', book_list, name='book_list'),
    path('AddBook', add_book, name='add_book'),
    path('editbook/', editbookview, name='editbook'),
    path('editbook/edit', edit_book),
    path('deletebook', delete_book, name='delete_book'),
    path('Borrowed',borrowed, name='borrowed'),
    path('ban',banstudent),
    path('searchBook', book_list_view)
] 
