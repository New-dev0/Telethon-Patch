# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0

__author__ = "New-Dev0"
__version__ = "0.1"


def apply():
    from . import methods, custom, events
    from telethon import TelegramClient as client

    # Rename long name methods..
    client.read = client.send_read_acknowledge
