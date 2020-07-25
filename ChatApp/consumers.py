import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from . models import ChatBox
from datetime import datetime
from SocialCred.models import UserInfo, User

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        receiver = self.scope['url_route']['kwargs']['username']
        sender = self.scope['user']
        print("s ", sender, " receiver ", receiver)
        await self.channel_layer.group_add(
            "gossip",
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept",
        })
        # await asyncio.sleep(10)


    async def websocket_receive(self, event):
        print("receive", event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')
            print(msg)
            user = self.scope['user']
            username = 'default'

            if user.is_authenticated:
                username = user.username
            myResponse = {
                'message': msg,
                'username': username,
                'time': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            }
            await self.create_chat(msg)
            await self.channel_layer.group_send("gossip",
                                                {
                                                    "type": "chat_message",
                                                    "text": json.dumps(myResponse)
                                                })

    async def chat_message(self, event):
        print("message", event)
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    @database_sync_to_async
    def create_chat(self, msg ):
        receiver = self.scope['url_route']['kwargs']['username']
        sender = self.scope['user']
        sndr = User.objects.get(username=sender)
        rec = User.objects.get(username=receiver)
        s =UserInfo.objects.get(usr=sndr)
        r =UserInfo.objects.get(usr=rec)
        return ChatBox.objects.create(sender=s, receiver=r, message=msg)


    async def websocket_disconnect(self, event):
        print("Disconnected", event)

