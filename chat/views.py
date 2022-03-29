from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from Users.models import CustomUser
from chat.models import ChatRoom, Chat

# def index(request):
#     return  render(request,'home.html')
from chat.utils import generate_roomname
from networks.models import Connection


class room(LoginRequiredMixin, View):

    def get(self, request, pk):
        rooms=[]
        room=ChatRoom.objects.all()
        for j in room:
            for i in j.user.all():
                if i.username==request.user.username:
                    rooms.append(j)
        chats = []
        chatsuser = []
        print(rooms)
        try:
            try:
                room = ChatRoom.objects.get(id=pk)

                for i in room.chat_set.all():
                    chats.append(i)
                    if i.user.username != request.user.username:
                        chatsuser=i.user
                #chats.reverse()
                room_name = room.name
                if room.last!=str(request.user.username):
                    room.notification=False
                    room.save()

                if request.user in room.user.all():
                    return render(request, 'chatroom.html', {'room_name': room_name, 'chats': chats,'chatsuser':chatsuser,'rooms':rooms})
                else:
                    return redirect('/')
            except:

                room=''
                k=CustomUser.objects.get(id=pk)

                x=list(ChatRoom.objects.filter(user=request.user))

                for j in x:
                    for c in j.user.all():
                        if c.username==k.username:
                            room=j

                print("cc",room)
                for i in room.chat_set.all():
                    chats.append(i)
                    if i.user.username != request.user.username:
                        chatsuser=i.user.username
                #chats.reverse()
                # room_name = room.name
                # room.notification=False
                if room.last!=str(request.user.username):
                    room.notification=False

                room.save()
                if request.user in room.user.all():
                    return redirect('/chat/'+str(room.id))
                else:
                    return redirect('/')

        except:
            print("x")
            room = ChatRoom.objects.create(name=generate_roomname())
            k = CustomUser.objects.get(id=pk)
            room.save()
            room.user.add(request.user)
            room.user.add(k)
            room.save()

            chats.reverse()
            # room_name = room.name
            if request.user in room.user.all():
                return redirect('/chat/'+str(room.id))
            else:
                return redirect('/')


