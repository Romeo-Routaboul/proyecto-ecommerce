from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'nombre', 'apellido']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('nombre', 'apellido')}),
    ) #this will allow to change these fields in admin module


admin.site.register(MyUser, MyUserAdmin)