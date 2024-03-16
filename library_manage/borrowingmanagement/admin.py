from django.contrib import admin
from .models import BorrowedBook

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ['user', 'borrow_date']

    def __str__(self):
        return self.title