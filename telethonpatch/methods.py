# GNU V3
# https://github.com/New-dev0/Telethon-Patch
# Copyright  New-dev0

import datetime
from typing import Optional

from telethon import TelegramClient

from telethon.tl import functions, types
from telethon.tl.alltlobjects import tlobjects

fns = {}
for obj in tlobjects.values():
    if "functions." in str(obj):
        fns.update({obj.__name__[:-7]: obj})


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
    self: "TelegramClient",
    peer: "TypeInputPeer",
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
            peer, rtmp_stream, title=title, schedule_date=schedule
        )
    )


async def join_group_call(
    self: "TelegramClient",
    call: "TypeInputGroupCall",
    join_as: "TypeInputPeer",
    params: "TypeDataJSON",
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
            call,
            join_as=join_as,
            params=params,
            muted=muted,
            video_stopped=video_stopped,
            invite_hash=invite_hash,
        )
    )


async def leave_group_call(
    self: "TelegramClient",
    call: "TypeInputGroupCall",
    source: int,
):
    """
    Leave a Group Call.

    Args:
       call:
       source:
    """
    return await self(functions.phone.LeaveGroupCallRequest(call, source=source))


async def discard_group_call(
    self: "TelegramClient",
    call: "TypeInputGroupCall",
):
    """
    Discard a Group Call.
    (You will need to have voice call admin previlege to start a call.)

    Args:
       call:
    """
    return await self(functions.phone.DiscardGroupCallRequest(call))


async def get_group_call(
    self: "TelegramClient",
    call: "TypeInputGroupCall",
    limit: int,
):
    """
    Get a Group Call.

    Args:
       call:
    """
    return await self(functions.phone.GetGroupCallRequest(call, limit=limit))


TelegramClient.create_group_call = create_group_call
TelegramClient.join_group_call = join_group_call
TelegramClient.leave_group_call = leave_group_call
TelegramClient.discard_group_call = discard_group_call
TelegramClient.get_group_call = get_group_call
