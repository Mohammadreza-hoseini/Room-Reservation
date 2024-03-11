from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Room
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class EmptyRoomListView(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'reservation/rooms_list.html'
    context_object_name = 'rooms_list'

    def get_queryset(self):
        return Room.objects.filter(status=False)


@login_required()
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.room = room
            comment.author = request.user
            comment.body = form.data['body']
            comment.rate = form.data['rate']
            comment.save()
            return render(request, 'reservation/room_detail.html', {'form': CommentForm(),
                                                                    'message': 'Your comment has been saved and will be'
                                                                               ' displayed after the administrator'
                                                                               ' approval'})
        return render(request, 'reservation/room_detail.html', {'room': room, 'form': form})
    else:
        return render(request, 'reservation/room_detail.html', {'room': room, 'form': CommentForm()})
