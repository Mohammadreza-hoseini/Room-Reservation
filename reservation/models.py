from django.db import models
from accounts.models import NewUser
import uuid


# Create your models here.

class Calendar(models.Model):
    id = models.CharField(default=uuid.uuid4, editable=False, primary_key=True)
    day = models.SmallIntegerField(verbose_name='choose day')  # choice field
    start_time = models.TimeField(verbose_name='start time', auto_now=False, auto_now_add=False)
    end_time = models.TimeField(verbose_name='end time', auto_now=False, auto_now_add=False)
    date = models.DateField(verbose_name='choose date')
    is_active = models.BooleanField(default=True, verbose_name='this time active or no')

    def __str__(self):
        return f'{self.day}: {self.start_time} - {self.end_time}'


class Room(models.Model):
    id = models.CharField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name='title of room')
    calendar_id = models.ManyToManyField(Calendar, related_name='room_calendar_id',
                                         verbose_name='choose day and time')
    status = models.BooleanField(default=False, verbose_name='status of room')
    created_at = models.DateTimeField(auto_now_add=True)
    capacity = models.SmallIntegerField(default=0, verbose_name='room capacity')

    def __str__(self):
        return self.status


class Reservation(models.Model):
    id = models.CharField(default=uuid.uuid4, editable=False, primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservation_room_id',
                                verbose_name='choose room')
    user_id = models.ManyToManyField(NewUser, related_name='reservation_user_id',
                                     verbose_name='choose user')
    status = models.BooleanField(default=False, verbose_name='reservation status')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id.phone_number}: {self.room_id.title}'
