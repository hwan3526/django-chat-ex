from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User

def index(request): 
    return render(request, 'index.html')

def room(request, room_name, username):
    user, created = User.objects.get_or_create(username=username)
    login(request, user)

    # 채팅 방으로 리디렉션
    return render(request, "room.html", {"room_name": room_name, "user": user})