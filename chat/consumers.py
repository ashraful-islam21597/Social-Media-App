import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import ChatRoom,Chat


class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        self.user_id = self.scope['user'].id
        #find room object
        room=await database_sync_to_async(ChatRoom.objects.get)(name=self.room_name)
        room.notification=True
        room.last=username


        #create new chat object
        chat=Chat(
            content= message,
            room=room,
            user=self.scope['user']

        )
        await database_sync_to_async(chat.save)()
        await database_sync_to_async(room.save)()

        await self.channel_layer.group_send(

            self.room_group_name,

            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
                'user_id': self.user_id
            }
        )


    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))