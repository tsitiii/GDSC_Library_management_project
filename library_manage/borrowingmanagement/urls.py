from django.urls import path
from .views import borrow_book

app_name = 'borrowingmanagement'

urlpatterns = [
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),

]
