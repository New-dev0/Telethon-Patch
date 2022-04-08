from telethon import events
from telethon.tl.types import UpdateBotChatInviteRequester
from telethon.tl.functions.messages import HideChatJoinRequestRequest
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
            if len(res.updates) == 1:
                return res.updates[0]
            return res

        async def reject(self):
            """Disapprove join request."""
            res = await self.client(
                HideChatJoinRequestRequest(
                    await self.get_input_chat(), user_id=self.user_id, approved=False
                )
            )
            if len(res.updates) == 1:
                return res.updates[0]
            return res

        async def get_user(self):
            return await self.client.get_entity(self.user_id)


setattr(events, "JoinRequest", JoinRequest)
