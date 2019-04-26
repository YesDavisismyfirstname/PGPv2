from channels.generic.websocket import AsyncWebsocketConsumer
import json
from apps.game_window.models import Lobbies


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    # Receive message from WebSocket

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        try:
            message = text_data_json['message']
        except:
            message = "NULL"
        try:
            UserJoined = text_data_json['UserJoined']
        except:
            UserJoined = "NULL"
        try:
            position = text_data_json['position']
        except:
            position = "NULL"
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'UserJoined': UserJoined,
                'position': position,
            }
        )
    # Receive message from room group

    async def chat_message(self, event):
        message = event['message']
        UserJoined = event['UserJoined']
        try: 
            position = event['position']
        except:
            position = ""
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'UserJoined': UserJoined,
            'position': position,
        }))
