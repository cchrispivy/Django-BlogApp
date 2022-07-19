from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from input_mask.widgets import InputMask



class SSNInput(InputMask):
    mask = {'mask': '999-99-9999'}

class UserRegisterForm(UserCreationForm):
    pk = forms.IntegerField()
    email = forms.EmailField()
    #ssn = SSNInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

