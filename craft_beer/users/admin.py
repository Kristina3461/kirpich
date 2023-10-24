from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username',)
    list_filter = ('username', 'email')
    ordering = ('username',)
