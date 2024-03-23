from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import User

admin.site.site_header = 'Library Management System'
admin.site.site_title = 'Library Management System'
admin.site.index_title = 'Welcome to the Library Management System'

class CustomUserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'is_admin', 'is_student', 'is_superuser','is_banned']
    list_filter = ['is_admin', 'is_student', 'is_superuser', 'is_banned']
    search_fields = ['username', 'email']
    actions = ['make_admin', 'make_student', 'ban_student']

    def make_admin(self, request, queryset):
        queryset.update(is_admin=True, is_student=False)

    make_admin.short_description = "Make selected user/users admin"

    def make_student(self, request, queryset):
        queryset.update(is_student=True, is_admin=False)

    make_student.short_description = "Make selected user/users student"

    def ban_student(self, request, queryset):
        queryset.update(is_student=True, is_banned=True)
    
    ban_student.short_description = "Ban selected User/Users"

    def has_change_permission(self, request, obj=None):
        if obj and obj.is_superuser:
            return False  # Super admins can't be edited
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.is_superuser:
            return False  # Super admins can't be deleted
        return super().has_delete_permission(request, obj)

admin.site.register(User, CustomUserAdmin)

