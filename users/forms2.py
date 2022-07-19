from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Submit, HTML

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Field('ssn', onkeyup="ssnFormatter()"),
                Fieldset(
                    '',
                    'first_name',
                    'last_name',
                    'email',
                    'username',
                    'password1',
                    'password2',
                    HTML("""
            <p>We use notes to get better, <strong>please help us {{ username }}</strong></p>
        """),
                    ),
                )

