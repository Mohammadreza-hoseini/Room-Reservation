from django import forms
from django.core.exceptions import ValidationError
from accounts.models import Comment, TeamLeader, TeamMembers
from .models import Calendar, Reservation, Room


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rate',)

    def clean_body(self):
        body = self.cleaned_data['body']
        if body is None or body == '':
            self.add_error('body', 'Enter your comment text')
        return body

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate is None or rate == '':
            self.add_error('rate', 'Select rate')
        return rate


class CalendarSelectForm(forms.Form):
    calendar_choices = forms.ModelChoiceField(queryset=None)

    def __init__(self, room_id, *args, **kwargs):
        self.room_id = room_id
        self.request = kwargs.pop('request', None)
        super(CalendarSelectForm, self).__init__(*args, **kwargs)
        self.fields['calendar_choices'].queryset = Calendar.objects.filter(room_calendar_id__id=room_id,
                                                                           is_active=True)

    def clean(self):
        get_team_leader = TeamLeader.objects.filter(leader_id=self.request.user.id)
        if not get_team_leader.exists():
            self.add_error('calendar_choices', 'Just leader can reserve room')
        else:
            check_user_count = TeamMembers.objects.filter(leader_id=get_team_leader.first().id).first()
            room_capacity = Room.objects.get(id=self.room_id)
            if room_capacity.capacity < check_user_count.users.all().count():
                raise ValidationError('The number of people is more than the capacity of the room')

    def save(self):
        get_leader = TeamLeader.objects.filter(leader_id=self.request.user.id).first()
        add_reserve = Reservation.objects.create(room_id_id=self.room_id.__str__(), leader_id=get_leader.id)
        add_reserve.save()
        get_calendar = self.cleaned_data['calendar_choices']
        get_calendar.is_active = False
        get_calendar.save()
        get_room = Room.objects.get(id=self.room_id.__str__())
        if not get_room.calendar_id.all().filter(is_active=True).exists():
            get_room.status = True
            get_room.save()
