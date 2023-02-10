from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'fullname', 'gender']
    search_fields = ['email', 'fullname']
    ordering = ['fullname']
    fieldsets = (
        (_('Personal information'), {
            'fields': ('email', 'fullname', 'national_code', 'home', 'phone', 'birthdate', 'gender', 'address', 'get_newsletter')
        }),
        (_('Date information'), {
            'fields': ('date_joined', 'last_login')
        }),
        (_('Other information'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'fullname', 'national_code', 'home', 'phone', 'birthdate', 'gender', 'address', 'get_newsletter'
            )
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
