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
    if request.method == 'GET':
        room = get_object_or_404(Room, id=room_id)
        get_comments = Comment.objects.filter(room_id=room.id, status=True)
        calendar_form = CalendarSelectForm(room_id)
        return render(request, 'reservation/room_detail.html',
                      {'room': room, 'form': CommentForm(), 'comments': get_comments, 'calendar_form': calendar_form})

    if request.method == 'POST':
        leader_user_list = TeamLeader.objects.all().values_list('leader__email')
        # ای دی اتاریخی که انتخاب شده را در میاریم
        calendar_chosen_id = dict(request.POST).get("calendar_choices")[0]
        # اینجا چک میکنیم که ایا که ایا یوزری که الان باهاش لاگین هستش جزور lead ها هستش یا نه

        leader_data = [i[0] for i in list(leader_user_list)]
        for i in leader_data:
            # اگر یوزری که باهاش لاگین کردیم جزو leader ها بود
            if str(request.user) == i:
                Calendar.objects.filter(id=calendar_chosen_id).update(is_active=True)
                # a = Room.objects.filter(id=room_id)
                b = Calendar.objects.filter(room_calendar_id=room_id, is_active=False).count()
                if b <= 0:
                    Room.objects.filter(id=room_id).update(status=True)

                return redirect('http://localhost:8000/')


@login_required()
def add_comment(request, room_id):
    print(room_id)
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
                          {'room': room, 'form': form, 'comments': get_comments})
    else:
        return render(request, 'reservation/room_detail.html',
                      {'room': room, 'form': CommentForm(), 'comments': get_comments})
