from django import forms

from accounts.models import Comment


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
