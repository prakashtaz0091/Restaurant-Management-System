# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Specify the custom model
    model = User
    
    # # Optional: Update list_display to show new fields in the user list
    # list_display = ('username', 'email','role', 'is_staff')

    # Extend the standard fieldsets to include new fields for editing
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {
            'fields': ('role',),
        }),
    )

    # Extend add_fieldsets to include new fields for user creation
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Info', {
            'fields': ('role', ),
        }),
    )

# # Register the custom admin class with the custom user model
# admin.site.register(User, CustomUserAdmin)   