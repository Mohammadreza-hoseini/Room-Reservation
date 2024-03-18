from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('rooms/', views.EmptyRoomListView.as_view(), name='rooms'),
    path('room_detail/<uuid:room_id>/', views.room_detail, name='room_detail'),
    path('add_comment/<uuid:room_id>/', views.add_comment, name='add_comment'),
    path('reserve_room/<uuid:room_id>/', views.reserve_room, name='reserve_room'),
]
