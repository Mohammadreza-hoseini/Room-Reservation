from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class EmptyRoomListView(ListView):
    model = Room
    template_name = 'reservation/rooms_list.html'
    context_object_name = 'rooms_list'

    def get_queryset(self):
        return Room.objects.filter(status=False)


# class RoomStatusView(DetailView):
#     model = Room
#     template_name = 'room_status.html'
#     context_object_name = 'room'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         room = self.get_object()
#         reservation_status = "Reserved" if room.status else "Empty"
#         context['reservation_status'] = reservation_status
#         return context
