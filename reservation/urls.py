from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('empty_rooms/', views.EmptyRoomListView.as_view(), name='empty_rooms'),
]
