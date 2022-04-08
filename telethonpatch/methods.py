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

async def start_group_call(
    self: "TelegramClient",
    peer: "types.InputPeer",
    rtmp_stream: bool = None,
    title: str = "",
    schedule=None,
):
    """
    Start or Schedule a Group Call.
    (You will need to have voice call admin previlege to start a call.)

    Args:
       peer: ChatId/Username of chat.
       title: Title to keep for voice chat.
       schedule (optional): 'datetime' object to schedule call.
    """
    return await self(
        functions.phone.CreateGroupCallRequest(
            peer, rtmp_stream, title=title, schedule_date=schedule
        )
    )


TelegramClient.start_group_call = start_group_call
