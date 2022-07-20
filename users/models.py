from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length = 200, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    ssn = models.CharField(max_length=11)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.customuser.username} Profile'



