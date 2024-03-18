from django.test import TestCase


from reservation.models import Room


class testRoomDetailView(TestCase):
    fixtures = [
        "newUser_data.json",
        "calendar_data.json",
        "rooms_data.json",
    ]

    # TODO
    # use client obj in TestCase
    def test_post_method(self):
        room_id = 1001
        url = f"room_detail/{room_id}/"
        # TODO
        # response = self.client.get(url, data=)
