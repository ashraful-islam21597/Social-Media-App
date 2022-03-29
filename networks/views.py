from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from Users.models import CustomUser, profile
from networks.models import Connection, Network

def accept_request(request,pk):
    user_self = CustomUser.objects.get(id=request.user.pk)

    c=Connection.objects.get(pk=pk)
    print(c)
    c.connected=True
    c.save()
    print(c.connected)
    c1=Connection.objects.get(network_id=c.profiles.user.network.id,profiles_id=user_self.network.id)
    print(c1)
    c1.connected=True
    c1.save()
    c.sent_request_for_connection=False
    c1.request_for_connection=False
    c.network.sent_request=c.network.sent_request-2
    c1.network.friend_request=c1.network.friend_request-2


    return redirect('/friends/' + str(request.user.pk))

def addfriend(request, pk):
    user_friend = Network.objects.get(pk=pk)

    user_self = CustomUser.objects.get(id=request.user.pk)

    c = Connection.objects.create(network_id=user_friend.id, profiles=user_self.profile, sent_request_for_connection=True)

    c1 = Connection.objects.create(network_id=user_self.network.id, profiles=user_friend.user.profile,
                                   request_for_connection=True)

    #c.save()
    #c.network.sent_request += 1
    #c.network.save()
    #c1.save()
    #c1.network.friend_request += 1
    #c1.network.save()
    return redirect('/friends/' + str(request.user.pk))



