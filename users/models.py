from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from PIL import Image
import numpy as np

class CustomUser(AbstractUser):
    username = models.CharField(max_length = 200, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    ssn = models.CharField(max_length = 200)
    last_four_ssn = models.CharField(max_length = 200)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        sqrWidth = np.ceil(np.sqrt(img.size[0]*img.size[1])).astype(int)
        img = img.resize((sqrWidth, sqrWidth))
        img.save(self.image.path)
