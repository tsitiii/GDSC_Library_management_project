from django.urls import path
from .views import borrow_book, profile_view,return_book

app_name = 'borrowingmanagement'

urlpatterns = [
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('profile',profile_view, name='profile_view'),
    path('Return/<int:book_id>/', return_book, name='Return')
]
