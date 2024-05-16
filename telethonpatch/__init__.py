# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0


from telethon.tl.alltlobjects import LAYER

__author__ = "New-Dev0"
__version__ = "0.04b0"


from . import methods, custom, events, pyrogram, inlinebuilder
from telethon import TelegramClient as BaseTelegramClient


class TelegramClient(
    BaseTelegramClient,
    methods.GroupCallMethods,
    methods.TopicMethods,
    pyrogram.PyrogramMethods,
):
    read = BaseTelegramClient.send_read_acknowledge
    send_poll = pyrogram.send_poll

    # map with methods
    vote_poll = pyrogram.vote_poll
    send_sticker = pyrogram.send_document
    send_video = pyrogram.send_document
    send_document = pyrogram.send_document
    send_voice = pyrogram.send_document

    leave_chat = BaseTelegramClient.delete_dialog
    get_chat = BaseTelegramClient.get_entity
    resolve_peer = BaseTelegramClient.get_input_entity
    run = BaseTelegramClient.run_until_disconnected

    # Rename long name methods..


def print_conf():
    print(f"Using Telethon-Patch (v{__version__}) [{LAYER}]")


print_conf()
