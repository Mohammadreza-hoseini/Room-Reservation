from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.


class NewUser(AbstractUser):
    id = models.CharField(default=uuid.uuid4, editable=False, primary_key=True)
    avatar = models.ImageField(upload_to='profile_images', null=True, blank=True, verbose_name='profile image')
    phone_number = models.CharField(verbose_name='phone number')
    otp = models.PositiveBigIntegerField(verbose_name='otp code', null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-date_joined',)


class TeamLeader(models.Model):
    id = models.CharField(default=uuid.uuid4, editable=False, primary_key=True)
    leader = models.OneToOneField(NewUser, on_delete=models.CASCADE, related_name='team_leader_user',
                                  verbose_name='Leader')
    users = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='users_of_team')

    def __str__(self):
        return self.leader.first_name


from reservation.models import Room


class ChooseRate(models.IntegerChoices):
    one = 1, "one"
    two = 2, "two"
    three = 3, "three"
    four = 4, "four"
    five = 5, "five"


class Comment(models.Model):
    id = models.CharField(default=uuid.uuid4, editable=False, primary_key=True)
    body = models.TextField(verbose_name='comment text')
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE, verbose_name='comment author',
                               related_name='comment_author_id')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='select room', related_name='comment_room_id')
    status = models.BooleanField(default=False, verbose_name='comment display')
    rate = models.PositiveSmallIntegerField(
        default=ChooseRate.five, choices=ChooseRate.choices, verbose_name="select rate"
    )

    def __str__(self):
        return self.body
