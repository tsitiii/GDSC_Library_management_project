from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import User
admin.site.register(User)
# class CustomUserAdmin(BaseUserAdmin):
#     list_display = ['username', 'email', 'is_admin', 'is_student', 'is_superuser']
#     list_filter = ['is_admin', 'is_student', 'is_superuser']
#     search_fields = ['username', 'email']
#     actions = ['make_admin', 'make_student']

#     def make_admin(self, request, queryset):
#         queryset.update(is_admin=True, is_student=False)

#     make_admin.short_description = "Make selected user/users admin"

#     def make_student(self, request, queryset):
#         queryset.update(is_student=True, is_admin=False)

#     make_student.short_description = "Make selected user/users student"

#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             obj.password = make_password(form.cleaned_data['password'])
#         obj.save()

#     # Customize admin view permissions based on user roles
#     def has_change_permission(self, request, obj=None):
#         if obj and obj.is_superuser:
#             return False  # Super admins can't be edited
#         return super().has_change_permission(request, obj)

#     def has_delete_permission(self, request, obj=None):
#         if obj and obj.is_superuser:
#             return False  # Super admins can't be deleted
#         return super().has_delete_permission(request, obj)

# # Register the custom UserAdmin class
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)