"""
Example of full functioning bot with Telethon-Patch

Fill API_ID, API_HASH and BOT_TOKEN in your env variables.
"""

import os

import telethonpatch

telethonpatch.apply()

import logging

logging.basicConfig(level=logging.INFO)

from telethon import TelegramClient
from telethon.events import JoinRequest

client = TelegramClient(
    "bot", api_id=int(os.getenv("API_ID")), api_hash=os.getenv("API_HASH")
)
client.start(bot_token=os.getenv("BOT_TOKEN"))


@client.on(JoinRequest())
async def example(request):
    await request.approve()


with client:
    client.run_until_disconnected()
