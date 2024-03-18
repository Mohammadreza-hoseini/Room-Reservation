from django.test import TestCase
from django.test.client import RequestFactory


from accounts.models import Comment as Comment
from reservation.models import Room

from reservation.forms import CommentForm, CalendarSelectForm


class CommentFormTest(TestCase):

    fixtures = ["comment_data.json"]

    def test_empty_body_should_return_error(self):
        comment_obj = Comment.objects.get(id=4001)
        form = CommentForm(
            data={"body": comment_obj["body"], "rate": comment_obj["rate"]}
        )
        self.assertEqual(form.errors["body"], ["Enter your comment text"])

    def test_none_body_should_return_error(self):
        comment_obj = Comment.objects.get(id=4001)
        form = CommentForm(data={"rate": comment_obj["rate"]})
        self.assertEqual(form.errors["body"], ["Enter your comment text"])

    def test_empty_rate_should_return_error(self):
        comment_obj = Comment.objects.get(id=4002)
        form = CommentForm(
            data={"body": comment_obj["body"], "rate": comment_obj["rate"]}
        )
        self.assertEqual(form.errors["rate"], ["Select rate"])

    def test_none_rate_should_return_error(self):
        comment_obj = Comment.objects.get(id=4001)
        form = CommentForm(data={"body": comment_obj["body"]})
        self.assertEqual(form.errors["rate"], ["Select rate"])


class CalendarSelectFormTest(TestCase):
    fixtures = [
        "calendar_data.json",
        "rooms_data.json",
        "newUser_data.json",
        "teamLeader_data.json",
    ]

    def setUpTest(self):
        self.factory = RequestFactory()


    #TODO
    # def test_teamLeader_exists(self):
    #     room_id = 1001
    #     url = f"add_comment/{room_id}/"
    #     request = self.factory.post(url, data=...)
    #     form = CalendarSelectForm(request=request, data={"room_id": room_id})   
    #     teamLeader_id = ...