# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0

from telethon.tl import functions, types
from telethon.tl.custom import Button, Message
from telethon.tl.types import (
    InputKeyboardButtonUserProfile,
    KeyboardButtonSimpleWebView,
)

# Button


def mention(text, user):
    """Send Button with UserProfile mention.

    call 'get_input_entity' to fill in user parameter."""
    return InputKeyboardButtonUserProfile(text, user)


def web(text, url):
    """Send Button with WebView."""
    return KeyboardButtonSimpleWebView(text, url)

b_is_inline = Button._is_inline

def is_inline(button):
    """Check if Button is Inline."""
    if isinstance(button, (
        types.InputKeyboardButtonUserProfile,
        types.KeyboardButtonSimpleWebView
    )):
        return True
    return b_is_inline(button)

setattr(Button, "mention", mention)
setattr(Button, "web", web)
setattr(Button, "_is_inline", is_inline)

# Message


def message_link(self: "Message"):
    """Message link"""
    if self.chat.username:
        return f"https://t.me/{self.chat.username}/{self.id}"
    return f"https://t.me/c/{self.chat.id}/{self.id}"


setattr(Message, "message_link", property(message_link))


async def comment(self: "Message", *args, **kwargs):
    """Bound Method to comment."""
    if self._client:
        return await self._client.send_message(
            self.chat_id, comment_to=self.id, *args, **kwargs
        )


async def react(self: "Message", *args, **kwargs):
    """Bound method to react to messages"""
    if self._client:
        return await self._client.send_reaction(self.chat_id, self.id, *args, **kwargs)


setattr(Message, "comment", comment)
setattr(Message, "react", react)
