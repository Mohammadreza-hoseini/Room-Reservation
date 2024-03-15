from django import forms

from accounts.models import Comment
from .models import Calendar


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
        super(CalendarSelectForm, self).__init__(*args, **kwargs)
        self.fields['calendar_choices'].queryset = Calendar.objects.filter(room_calendar_id__id=room_id,
                                                                           is_active=False)
