# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0

import datetime
from typing import Optional

from telethon import TelegramClient

from telethon.tl import functions, types
from telethon.tl.alltlobjects import tlobjects

fns = {
    obj.__name__[:-7]: obj
    for obj in tlobjects.values()
    if "functions." in str(obj)
}


def _getattr(self, item):
    if item in self.__dict__:
        return self.__dict__[item]
    if (item in fns) or (item[:-7] in fns):
        if item not in fns:
            item = item[:-7]
        fn_ = fns[item]

        async def function(*args, **kwargs):
            return await self(fn_(*args, **kwargs))

        return function
    raise AttributeError(f"{self.__class__.__name__} has no attribute '{item}'")


TelegramClient.__getattr__ = _getattr


async def create_group_call(
    self: TelegramClient,
    peer: types.TypeInputPeer,
    rtmp_stream: Optional[bool] = None,
    random_id: int = None,
    title: Optional[str] = None,
    schedule_date: Optional[datetime.datetime] = None,
):
    """
    Create or Schedule a Group Call.
    (You will need to have voice call admin previlege to start a call.)

    Args:
       peer: ChatId/Username of chat.
       rtmp_stream: Whether to start rtmp stream.
       random_id: Any random integer or leave it None.
       title: Title to keep for voice chat.
       schedule (optional): 'datetime' object to schedule call.
    """
    return await self(
        functions.phone.CreateGroupCallRequest(
            peer=peer,
            rtmp_stream=rtmp_stream,
            title=title,
            random_id=random_id,
            schedule_date=schedule_date,
        )
    )


async def join_group_call(
    self: TelegramClient,
    call: types.TypeInputGroupCall,
    join_as: types.TypeInputPeer,
    params: types.TypeDataJSON,
    muted: Optional[bool] = None,
    video_stopped: Optional[bool] = None,
    invite_hash: Optional[str] = None,
):
    """
    Join a Group Call.

    Args:
       call:
       join_as:
       params:
       muted:
       video_stopped:
       invite_hash:
    """
    return await self(
        functions.phone.JoinGroupCallRequest(
            call=call,
            join_as=join_as,
            params=params,
            muted=muted,
            video_stopped=video_stopped,
            invite_hash=invite_hash,
        )
    )


async def leave_group_call(
    self: TelegramClient,
    call: types.TypeInputGroupCall,
    source: int,
):
    """
    Leave a Group Call.

    Args:
       call:
       source:
    """
    return await self(functions.phone.LeaveGroupCallRequest(call=call, source=source))


async def discard_group_call(
    self: TelegramClient,
    call: types.TypeInputGroupCall,
):
    """
    Discard a Group Call.
    (You will need to have voice call admin previlege to start a call.)

    Args:
       call:
    """
    return await self(functions.phone.DiscardGroupCallRequest(call=call))


async def get_group_call(
    self: TelegramClient,
    call: types.TypeInputGroupCall,
    limit: int,
):
    """
    Get a Group Call.

    Args:
       call:
    """
    return await self(functions.phone.GetGroupCallRequest(call=call, limit=limit))


async def send_reaction(
    self: TelegramClient,
    peer: types.TypeInputPeer,
    msg_id: int,
    big: Optional[bool] = None,
    reaction: Optional[str] = None,
):
    """
    Send reaction to a message.

    Args:
       peer:
       msg_id:
       big:
       reaction:
    """
    return await self(
        functions.messages.SendReactionRequest(
            peer=peer,
            msg_id=msg_id,
            big=big,
            reaction=reaction,
        ),
    )


async def create_topic(
    self: TelegramClient,
    channel: types.InputChannel,
    title: str,
    icon_color: int = None,
    icon_emoji_id: int = None,
    random_id: int = None,
    send_as: types.TypeInputPeer = None,
):
    return await self(
        functions.channels.CreateForumTopicRequest(
            channel=channel,
            title=title,
            icon_color=icon_color,
            icon_emoji_id=icon_emoji_id,
            random_id=random_id,
            send_as=send_as,
        )
    )


async def edit_topic(
    self: TelegramClient,
    channel: types.InputChannel,
    topic_id: int,
    title: str = None,
    icon_emoji_id: int = None,
    closed: bool = None,
):
    return await self(
        functions.channels.EditForumTopicRequest(
            channel=channel,
            topic_id=topic_id,
            title=title,
            icon_emoji_id=icon_emoji_id,
            closed=closed,
        )
    )


async def get_topics(
    self: TelegramClient,
    channel: types.InputChannel,
    offset_date: Optional[datetime.datetime] = None,
    offset_id: int = None,
    offset_topic: int = None,
    limit: int = None,
    q: Optional[str] = None,
    topics: int = None,
):
    if topics is None:
        return await self(
            functions.channels.GetForumTopicsRequest(
                channel=channel,
                offset_date=offset_date,
                offset_id=offset_id,
                offset_topic=offset_topic,
                limit=limit,
                q=q,
            )
        )
    else:
        return await self(
            functions.channels.GetForumTopicsByIDRequest(channel=channel, topics=topics)
        )

async def join_chat(
    self: TelegramClient,
    entity: types.InputChannel = None,
    hash: str = None
):
    if entity:
        return await self(functions.channels.JoinChannelRequest(entity))
    elif hash:
        return await self(functions.messages.ImportChatInviteRequest(hash))
    else:
        raise ValueError("Either entity or hash is required.")



TelegramClient.create_group_call = create_group_call
TelegramClient.join_group_call = join_group_call
TelegramClient.leave_group_call = leave_group_call
TelegramClient.discard_group_call = discard_group_call
TelegramClient.get_group_call = get_group_call
TelegramClient.send_reaction = send_reaction
TelegramClient.create_topic = create_group_call
TelegramClient.edit_topic = edit_topic
TelegramClient.get_topics = get_topics
TelegramClient.join_chat = join_chat