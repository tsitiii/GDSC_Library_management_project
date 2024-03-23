from django.urls import path
from .views import borrow_book, profile_view

app_name = 'borrowingmanagement'

urlpatterns = [
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('profile',profile_view, name='profile_view'),
]
