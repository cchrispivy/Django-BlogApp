from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

class CustomUser(AbstractUser):
    username = models.CharField(max_length = 200, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    ssn = models.CharField(max_length = 200)

    def __str__(self):
        return self.username

@receiver(post_save, sender=CustomUser)
def encrypt_ssn_receiver(sender, instance, created, *args, **kwargs):
    if created:
        encoded_ssn = bytes(instance.ssn, 'utf-8')
        instance.ssn = cipher_suite.encrypt(encoded_ssn)
        instance.save(update_fields=['ssn'])


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.customuser.username} Profile'



