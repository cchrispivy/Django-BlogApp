from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission
from django import forms
from .models import Profile, CustomUser
from .crypt_util import *

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    change_form_template = 'change_form.html'

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('decrypted_ssn',)}),
    )

    readonly_fields = ('decrypted_ssn', )

    def decrypted_ssn(self, instance):
        token = instance.ssn
        decrypted = decrypt(token.encode('utf-8'))
        return decrypted.decode('utf-8')
    decrypted_ssn.short_description = "SSN"

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

