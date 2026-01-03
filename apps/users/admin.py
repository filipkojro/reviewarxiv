from django.contrib import admin

from apps.users.models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class UserAdmin(CustomUser):
    pass