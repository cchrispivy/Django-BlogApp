from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission
from django import forms
from .models import Profile, CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    change_form_template = 'change_form.html'

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('ssn',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

