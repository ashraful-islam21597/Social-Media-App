from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver

from Users.models import CustomUser, profile
from chat.models import ChatRoom
from chat.utils import generate_roomname
from networks.models import Network, Connection


@receiver(post_save,sender=CustomUser)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        Network.objects.create(user=instance,)
        profile.objects.create(user=instance,)





@receiver(pre_delete,sender=Connection)
def post_save_deletefriend(sender,instance,**kwargs):

    print(instance.network.user)
    print(instance.profiles.user)

    if instance.request_for_connection==True and instance.sent_request_for_connection==False:
        instance.network.sent_request=instance.network.sent_request-(1)
        instance.network.save()
    elif instance.sent_request_for_connection==True and instance.request_for_connection==False:
        instance.network.friend_request=instance.network.friend_request-(1)
        instance.network.save()

@receiver(post_save,sender=Connection)
def post_save_addfriend(sender,instance,created,**kwargs):


    if instance.request_for_connection==True and instance.sent_request_for_connection==False:
        instance.network.sent_request=instance.network.sent_request+(1)
        instance.network.save()
    elif instance.sent_request_for_connection==True and instance.request_for_connection==False:
        instance.network.friend_request=instance.network.friend_request+(1)
        instance.network.save()
    # else:
    #     ChatRoom.objects.create(name=generate_roomname(),connection=instance)

    # if instance.sent_request_for_connection==False:
    #     instance.sent_request_for_connection= True
    #     instance.network.sent_request=instance.network.sent_request+1
    #     instance.network.save()
    # elif instance.profiles.user.request_for_connection==False:
    #     instance.profiles.user.request_for_connection=True
    #     instance.profiles.user.network.friend_request=instance.network.friend_request+1
    #     instance.network.save()

    