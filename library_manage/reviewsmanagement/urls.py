from django.urls import path
from . import views

app_name = 'reviewsmanagement'

urlpatterns = [
    path('book_detail/<str:book_title>/', views.book_detail, name='book_detail'),
    path('edit_review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]
