from django.urls import path
from .views import (

    chat,
    chat_box,
    sendMessage,
    recieveMessage,

)

urlpatterns = [
    path('', chat, name='chat-show'),
    path('<int:pk>/', chat_box, name='chat'),
    path('<int:pk>/send/message', sendMessage, name='send-message'),
    path('<int:pk>/recieveMessage', recieveMessage, name='recieve-message'),
]