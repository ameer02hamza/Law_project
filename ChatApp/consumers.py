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
        await asyncio.sleep(10)
        await self.send({
            "type": "websocket.send",
            "text": " I am ameer hamza",
        })

    async def websocket_receiver(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("Disconnected", event)

