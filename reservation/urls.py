from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('rooms/', views.EmptyRoomListView.as_view(), name='rooms'),
]
