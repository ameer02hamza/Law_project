import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from . models import ChatBox

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept",
        })
        receiver = self.scope['url_route']['kwargs']['username']
        sender = self.scope['user']
        print("s ",sender, " receiver ", receiver)
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
                'message':msg,
                'username':username
            }
            await self.send({
                "type": "websocket.send",
                "text": json.dumps(myResponse)
            })

    async def websocket_disconnect(self, event):
        print("Disconnected", event)

