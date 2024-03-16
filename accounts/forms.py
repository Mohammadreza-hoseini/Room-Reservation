import re
import random

from django.core.exceptions import ValidationError
from django.utils import timezone
from django import forms
from .models import NewUser, TeamLeader, TeamMembers


class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('first_name', 'last_name', 'email', 'phone_number',)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name is None or first_name == '':
            self.add_error('first_name', 'Enter your firstname')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name is None or last_name == '':
            self.add_error('last_name', 'Enter your last_name')
        return last_name

    def clean_email(self):
        email = self.cleaned_data['email']
        if email is None or email == '':
            self.add_error('email', 'Enter your email')
            return False
        pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        result = bool(pattern.match(email))
        if result is False:
            self.add_error('email', 'Email format is wrong')
        check_email = NewUser.objects.filter(email=email).first()
        if check_email:
            self.add_error('email', 'This email exist')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number is None or phone_number == '':
            self.add_error('phone_number', 'Enter your phone number')
            return False
        pattern = '^(\+98|0)?9\d{9}$'
        result = re.match(pattern, str(phone_number))
        if not result:
            self.add_error('phone_number', 'Phone number format is wrong')
        check_phone_number = NewUser.objects.filter(phone_number=phone_number).first()
        if check_phone_number:
            self.add_error('phone_number', 'This phone number exist')
        return phone_number

    def save(self, commit=True):
        data = self.data
        user = NewUser.objects.create(first_name=data.get('first_name'),
                                      last_name=data.get('last_name'),
                                      email=data.get('email'),
                                      username=data.get('phone_number'),
                                      phone_number=data.get('phone_number'))
        user.save()


class LoginForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('phone_number',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number is None or phone_number == '':
            self.add_error('phone_number', 'Enter your phone number')
            return False
        pattern = '^(\+98|0)?9\d{9}$'
        result = re.match(pattern, str(phone_number))
        if not result:
            self.add_error('phone_number', 'Phone number format is wrong')
        check_phone_number = NewUser.objects.filter(phone_number=phone_number).first()
        if not check_phone_number:
            self.add_error('phone_number', 'SignUp please')
        elif check_phone_number:
            check_phone_number.otp = random.randint(10000, 99999)
            check_phone_number.otp_expire = timezone.now() + timezone.timedelta(seconds=30)
            print(check_phone_number.otp)
            check_phone_number.save()
        return phone_number


class OtpForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('otp',)

    def clean_otp(self):
        otp = self.cleaned_data['otp']
        if otp is None or otp == '':
            self.add_error('otp', 'Enter otp code')
        return otp


class AvatarForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('avatar',)


class TeamMembersForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TeamMembersForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TeamMembers
        fields = ('leader',)

    def clean(self):
        query = TeamMembers.objects.filter(users__id=self.request.user.id,
                                           leader_id=self.cleaned_data['leader'].id).first()
        if query:
            self.add_error('leader', 'You are a member of one group and you cannot join another group.')
        else:
            add_to_team = TeamMembers.objects.create(leader_id=self.cleaned_data['leader'].id)
            add_to_team.users.add(NewUser.objects.get(id=self.request.user.id))
            add_to_team.save()
