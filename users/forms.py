from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from input_mask.widgets import InputMask

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, *kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['email'].label = "Email"
        self.fields['ssn'].label = "SSN"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = " Confirm Password"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

        self.fields['ssn'].widget.attrs.update(
            {
                'id': 'ssn',
                'placeholder': 'Enter SSN',
            }
        )
    
    email = forms.EmailField()
    ssn = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'ssn', 'password1', 'password2']



