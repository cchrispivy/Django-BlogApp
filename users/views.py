from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cryptography.fernet import Fernet
from .forms import UserRegisterForm

def register(request):
    key = Fernet.generate_key()
    crypter = Fernet(key)

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            ssn = form.cleaned_data.get('ssn')
            encrypted_ssn = crypter.encrypt(str.encode(ssn))
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
