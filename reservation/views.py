from django.shortcuts import render
from .models import * 
from django.views.generic import ListView

class EmptyRoomListView(ListView):

    model = Room
    context_object_name = 'empty_room_list'
    queryset = Room.objects.filter(status=False)
    