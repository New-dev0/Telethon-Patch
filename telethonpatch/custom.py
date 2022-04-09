# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0

from telethon.tl import functions
from telethon.tl.custom import Button, Message
from telethon.tl.types import KeyboardButtonUserProfile

# Button


def mention(text, user):
    """Send Button with UserProfile mention.

    call 'get_input_entity' to fill in user parameter."""
    return KeyboardButtonUserProfile(text, user)


setattr(Button, "mention", mention)

# Message


def message_link(self: "Message"):
    """Message link"""
    if self.chat.username:
        return f"https://t.me/{self.chat.username}/{self.id}"
    return f"https://t.me/c/{self.chat.id}/{self.id}"


Message.message_link = property(message_link)


async def comment(self: "Message", *args, **kwargs):
    """Bound Method to comment."""
    if self._client:
        return await self._client.send_message(
            self.chat_id, comment_to=self.id, *args, **kwargs
        )


async def react(self: "Message", reaction: str, big: bool = False):
    """Bound method to react to messages"""
    if self._client:
        return await self._client(
            functions.messages.SendReactionRequest(
                self.chat_id, self.id, big=big, reaction=reaction
            )
        )


Message.comment = comment
Message.react = react
