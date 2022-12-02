# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0


#from telethon.tl.alltlobjects import LAYER

__author__ = "New-Dev0"
__version__ = "0.2"


def apply():
    from . import methods, custom, events
    from telethon import TelegramClient

    # Rename long name methods..
    TelegramClient.read = TelegramClient.send_read_acknowledge
