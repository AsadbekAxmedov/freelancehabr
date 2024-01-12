from django.contrib import admin
from users.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'avatar', 'first_name', 'last_name')
    fields = ('username', 'role', 'avatar', 'first_name', 'last_name')