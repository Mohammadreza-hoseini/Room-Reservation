from django.shortcuts import render
from .models import * 
from django.views.generic import ListView

class EmptyRoomListView(ListView):

    model = Room
    template_name = 'empty_room_list.html'
    context_object_name = 'empty_room_list' 
    
    def get_queryset(self):
        return Room.objects.filter(status=False)