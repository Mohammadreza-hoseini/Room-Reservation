from django.shortcuts import render
from .models import Room
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class EmptyRoomListView(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'reservation/rooms_list.html'
    context_object_name = 'rooms_list'

    def get_queryset(self):
        return Room.objects.filter(status=False)
