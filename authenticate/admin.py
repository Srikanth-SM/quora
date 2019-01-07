from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = SignUpForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    list_display = ['username', 'email', ]


# admin.site.unregister(User)
admin.site.register(MyUser, MyUserAdmin)
