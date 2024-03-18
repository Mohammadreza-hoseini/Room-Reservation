from django.test import TestCase

from reservation.models import Reservation, Room
from accounts.models import TeamLeader


class ReservationModelTest(TestCase):

    fixtures = [
        "newUser_data.json",
        "teamLeader_data.json",
        "calendar_data.json",
        "rooms_data.json",
        "reservation_data.json",
    ]

    def test_room_id_label(self):
        reservation_obj = Reservation.objects.get(id=2001)
        field_label = reservation_obj._meta.get_field("room_id").verbose_name
        self.assertEqual(field_label, "choose room")

    def test_leader_label(self):
        reservation_obj = Reservation.objects.get(id=2001)
        field_label = reservation_obj._meta.get_field("leader").verbose_name
        self.assertEqual(field_label, "choose leader")
