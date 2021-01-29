from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    search_fields = ('emails', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'first_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',)}),
        ('Permisstions', {'fields': ('is_staff', 'is_active', 'groups')}),
        ('Personal', {'fields': ('telephone', 'city', 'address', 'activity',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
