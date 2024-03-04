from django.contrib import admin
from .models import Calendar, Room, Reservation

# Register your models here.

admin.site.register(Calendar)
admin.site.register(Room)
admin.site.register(Reservation)
