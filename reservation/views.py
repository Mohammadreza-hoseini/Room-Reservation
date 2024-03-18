from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from accounts.models import Comment, TeamLeader, TeamMembers, NewUser
from .forms import CommentForm, CalendarSelectForm
from .models import Room, Calendar
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
    if request.method == 'POST':
        room = get_object_or_404(Room, id=room_id)
        get_comments = Comment.objects.filter(room_id=room.id, status=True)
        return render(request, 'reservation/room_detail.html',
                      {'room': room, 'form': CommentForm(), 'comments': get_comments,
                       'calendar_form': CalendarSelectForm(room_id)})
    else:
        room = get_object_or_404(Room, id=room_id)
        get_comments = Comment.objects.filter(room_id=room.id, status=True)
        return render(request, 'reservation/room_detail.html',
                      {'room': room, 'form': CommentForm(), 'comments': get_comments,
                       'calendar_form': CalendarSelectForm(room_id)})


@login_required()
def reserve_room(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(Room, id=room_id)
        get_comments = Comment.objects.filter(room_id=room.id, status=True)
        calendar_form = CalendarSelectForm(room_id, request.POST, request=request)
        if calendar_form.is_valid():
            calendar_form.save()
            return render(request, 'home/home.html', {'message': 'The reservation was made successfully'})
        return render(request, 'reservation/room_detail.html',
                      {'room': room, 'comments': get_comments,
                       'calendar_form': CalendarSelectForm(room_id, request.POST, request=request),
                       'form': CommentForm()})
    else:
        return redirect('reservation:room_detail', room_id)


@login_required()
def add_comment(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    get_comments = Comment.objects.filter(room_id=room.id, status=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.room_id = room_id
            comment.author = request.user
            comment.body = form.data['body']
            comment.rate = form.data['rate']
            comment.save()
            return redirect('reservation:room_detail', room_id)
        else:
            return render(request, 'reservation/room_detail.html',
                          {'room': room, 'form': form, 'comments': get_comments,
                           'calendar_form': CalendarSelectForm(room_id)})
    else:
        return redirect('reservation:room_detail', room_id)
