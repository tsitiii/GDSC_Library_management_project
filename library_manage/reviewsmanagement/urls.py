from django.urls import path
from .views import review_list, add_review, edit_review, delete_review, book_detail

app_name = 'reviewsmanagement'

urlpatterns = [
    path('', review_list, name='review_list'),
    path('add/<int:book_id>/', add_review, name='add_review'),
    path('edit/<int:review_id>/', edit_review, name='edit_review'),
    path('delete/<int:review_id>/', delete_review, name='delete_review'),
    path('book-detail/<int:book_id>/', book_detail, name='book_detail'),
]
