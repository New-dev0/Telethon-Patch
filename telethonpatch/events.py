# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0

from telethon import events
from telethon.tl import types
from telethon.tl.types import UpdateBotChatInviteRequester
from telethon.tl.functions.messages import HideChatJoinRequestRequest
from telethon.tl.functions.phone import ToggleGroupCallRecordRequest
from telethon.events.common import EventCommon, name_inner_event, EventBuilder


@name_inner_event
class JoinRequest(EventBuilder):
    """
    Occurs on new Chat Join requests. (Bots only.)
    """

    @classmethod
    def build(cls, update, _, __):
        if isinstance(update, UpdateBotChatInviteRequester):
            return cls.Event(update)

    #        elif isinstance(update, MessageService) and isinstance(update.action, MessageActionChatJoinedByRequest):
    #            return cls.Event(update, approved=True)

    class Event(EventCommon):
        def __init__(self, update):
            super().__init__(chat_peer=update.peer)
            self._user_id = update.user_id
            self.invite = update.invite
            self.user_about = update.about

        @property
        def user_id(self):
            """user id of user"""
            return self._user_id

        @property
        def link(self):
            """Invite link"""
            return self.invite.link

        async def approve(self):
            """Approve Join request of a User"""
            res = await self.client(
                HideChatJoinRequestRequest(
                    await self.get_input_chat(), user_id=self.user_id, approved=True
                )
            )
            return res.updates[0] if len(res.updates) == 1 else res

        async def reject(self):
            """Disapprove join request."""
            res = await self.client(
                HideChatJoinRequestRequest(
                    await self.get_input_chat(), user_id=self.user_id, approved=False
                )
            )
            return res.updates[0] if len(res.updates) == 1 else res

        async def get_user(self):
            return await self.client.get_entity(self.user_id)


setattr(events, "JoinRequest", JoinRequest)


@name_inner_event
class GroupCall(EventBuilder):
    """
    Occurs on certain event like

    * Group call started
    * Group call ended
    * Group call scheduled."""

    @classmethod
    def build(cls, update, _, __):
        if isinstance(
            update, (types.UpdateNewMessage, types.UpdateNewChannelMessage)
        ) and isinstance(update.message, types.MessageService):
            update = update.message
            if isinstance(update.action, types.MessageActionGroupCall):
                return cls.Event(update, duration=update.action.duration or 0)
            elif isinstance(update.action, types.MessageActionGroupCallScheduled):
                return cls.Event(update, scheduled=True)

    class Event(EventCommon):
        def __init__(self, update, scheduled=None, duration=None):
            super().__init__(update.peer_id, update.id)
            self._update = update
            self._input_call = update.action.call
            self._scheduled = scheduled
            self.duration = duration
            self.started = None
            self.ended = None

            if duration == 0:
                self.started = True
            elif duration != None:
                self.ended = True

        @property
        def input_call(self):
            """returns 'InputGroupCall'"""
            return self._input_call

        @property
        def scheduled(self):
            """Whether Group call has been scheduled."""
            return self._scheduled

        async def start(self, *args, **kwargs):
            """Start Group call."""
            return await self.client.create_group_call(self.chat_id, *args, **kwargs)

        async def discard(self):
            """End Group call."""
            return await self.client.discard_group_call(self.input_call)

        async def toggle_record(
            self, start=None, video=None, video_portrait=None, title=None
        ):
            """Toggle group call record."""
            return await self.client(
                ToggleGroupCallRecordRequest(
                    self.input_call,
                    start=start,
                    video=video,
                    video_portrait=video_portrait,
                    title=title,
                )
            )


setattr(events, "GroupCall", GroupCall)
