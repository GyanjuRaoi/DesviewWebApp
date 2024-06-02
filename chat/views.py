from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from users.models import Profile, Friends
from .models import Message
from django.http.response import JsonResponse
import json


def chat(request):
    user = request.user

    profileList = []
    try:
        connect = Friends.objects.get(user= request.user)
        friendList = connect.friends.all()
        for i in friendList:
            profileList.append(i.profile)
    except:
        profileList = []

    context = {
        'profiles': profileList,
    }
    return render(request, 'chat/chat_show.html', context)


def chat_box(request, pk):
    sender_msg = request.user.profile
    try_user = User.objects.get(id= pk)
    receiver_msg = try_user.profile
    
    message = Message.objects.all()
    messages = Message.objects.filter(sender_message= receiver_msg, receiver_message= sender_msg)
    length_message = messages.count()

    profileList = []
    try:
        connect = Friends.objects.get(user= request.user)
        friendList = connect.friends.all()
        for i in friendList:
            print(i.profile.profile_picture.url)
            profileList.append(i.profile)
    except:
        profileList = []
   
    
    context = {
        "title": 'Chat',
        "message": message,
        "receiver": receiver_msg,
        "sender": sender_msg,
        "friend": try_user.id,
        "last_message_index": length_message,
        'profiles': profileList,
    }
    return render(request, 'chat/chat.html', context)

def sendMessage(request, pk):

    sender_msg = request.user.profile
    try_user = User.objects.get(id= pk)
    receiver_msg = try_user.profile
    message = json.loads(request.body)

    if message == "":
            pass
    else:
        create_message = Message.objects.create(sender_message= sender_msg, receiver_message= receiver_msg, text_body= message)
        
    return JsonResponse(message, safe=False)

def recieveMessage(request, pk):

    sender_user = request.user.profile
    try_user = User.objects.get(id= pk)
    receiver_user = try_user.profile

    messages = Message.objects.filter(sender_message= receiver_user, receiver_message= sender_user)

    empty_array_message = []

    for msg in messages:

        empty_array_message.append(msg.text_body)


    return JsonResponse(empty_array_message, safe= False)

