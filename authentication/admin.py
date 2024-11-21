from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Fields to display in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')

    # Fields to display on the user detail/edit page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

    # Fields to display on the user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'role'),
        }),
    )

# Register the custom User model and custom admin
admin.site.register(User, CustomUserAdmin)
