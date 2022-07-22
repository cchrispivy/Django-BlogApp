from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CustomUser, Profile
from .crypt_util import *

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=CustomUser)
def encrypt_ssn_receiver(sender, instance, created, *args, **kwargs):
    if created:
        token = bytes(instance.ssn, 'utf-8')
        encoded = encrypt(token)
        instance.last_four_ssn = '***-**-%s' % instance.ssn[-4:]
        instance.ssn = encoded.decode('utf-8')
        instance.save(update_fields=['ssn', 'last_four_ssn'])
