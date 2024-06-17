from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('username', 'email', 'name', 'age')
