import re
from django import forms
from .models import NewUser


class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('first_name', 'last_name', 'phone_number',)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name is None or first_name == '':
            self.add_error('first_name', 'Enter your firstname')

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name is None or last_name == '':
            self.add_error('last_name', 'Enter your last_name')

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

    def save(self, commit=True):
        data = self.data
        user = NewUser.objects.create(first_name=data.get('first_name'),
                                      last_name=data.get('last_name'),
                                      phone_number=data.get('phone_number'),
                                      username=data.get('phone_number'))
        user.save()
