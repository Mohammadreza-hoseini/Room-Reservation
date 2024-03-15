from django.test import TestCase

from reservation.models import Reservation, Room
from accounts.models import TeamLeader


class ReservationModelTest(TestCase):

    fixtures = ["reservation_data.json"]

    @classmethod
    def setUpTestData(cls):
        # all_rooms = Room.objects.all().count()
        # print("Debug:")
        # print(all_rooms)

        room_obj = Room.objects.get(title="first room")
        teamLeader_obj = TeamLeader.objects.get(leader__username="mohammad")
        Reservation.objects.create(room_id=room_obj, leader=teamLeader_obj)

    def test_room_id_label(self):
        reservation_obj = Reservation.objects.get(id=1)
        field_label = reservation_obj._meta.get_field("room_id").verbose_name
        self.assertEqual(field_label, "choose room")

    def test_leader_label(self):
        reservation_obj = Reservation.objects.get(id=1)
        field_label = reservation_obj._meta.get_field("leader").verbose_name
        self.assertEqual(field_label, "choose leader")
