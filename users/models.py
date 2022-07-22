from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from cryptography.fernet import Fernet
from .crypt_util import *

class CustomUser(AbstractUser):
    username = models.CharField(max_length = 200, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    ssn = models.CharField(max_length = 200)
    last_four_ssn = models.CharField(max_length = 11)

    def __str__(self):
        return self.username

@receiver(post_save, sender=CustomUser)
def encrypt_ssn_receiver(sender, instance, created, *args, **kwargs):
    if created:
        token = bytes(instance.ssn, 'utf-8')
        encoded = encrypt(token)
        instance.last_four_ssn = '***-**-%s' % instance.ssn[-4:]
        instance.ssn = encoded.decode('utf-8')
        instance.save(update_fields=['ssn'])


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.customuser.username} Profile'



