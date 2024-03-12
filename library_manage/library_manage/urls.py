
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),              
    path('books/', include('bookmanagement.urls')),  
    path('borrowings/', include('borrowingmanagement.urls')), 
    path('reviews/', include('reviewsmanagement.urls')),      
]
