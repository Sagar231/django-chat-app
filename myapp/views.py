from django.shortcuts import render
from . models import ChatRoom

# Create your views here.
def index(request):
    chatrooms = ChatRoom.objects.all()

    return render(request,'myapp/index.html',{"chatrooms":chatrooms})


def chatroom(request,slug):
    chatroom  = ChatRoom.objects.get(slug=slug) # why are we not using filter ##becuse get is used for single object with unique id
    return render(request,'myapp/room.html',{"chatroom":chatroom})
