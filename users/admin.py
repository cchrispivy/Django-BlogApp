from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, CustomUser

class CustomUserAdmin(CustomUser):
    #ssn = 
    pass



admin.site.register(CustomUser)
admin.site.register(Profile)

