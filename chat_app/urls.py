from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:room_name>/<str:username>/", views.room, name="room"),
]