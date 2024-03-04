from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.

class NewUser(AbstractUser):
    id = models.CharField(default=uuid.uuid4, editable=False, primary_key=True)
    phone_number = models.SmallIntegerField(verbose_name='phone number', unique=True, default=0)
    otp = models.SmallIntegerField(verbose_name='otp code', default=0)
    otp_expire = models.DateTimeField(blank=True, null=True, verbose_name='otp code expire time')
    avatar = models.ImageField(upload_to='profile_images', null=True, blank=True, verbose_name='profile image')
    reservation_count = models.SmallIntegerField(default=0, verbose_name='user reservations count')

    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ('-date_joined',)
