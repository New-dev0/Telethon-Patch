from telethon.client import TelegramClient
from typing import List
from telethon import hints, utils
from secrets import token_bytes
from telethon.tl.types import InputMediaPoll, TypePoll, PollAnswer
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import UpdateUsernameRequest as UpdateChatUsername
from telethon.tl.custom import Message


async def send_document(self: TelegramClient, chat_id, document, *args, **kwargs):
    await self.send_file(chat_id, document, *args, **kwargs)


async def send_poll(
    self: TelegramClient,
    chat_id: "hints.EntityLike",
    question: str,
    options,
    correct_answers=None,
    solution: str = "",
    schedule=None,
    is_anonymous: bool = True,
    closed: bool = False,
    multiple_choice: bool = False,
    quiz: bool = False,
    close_date=None,
):
    solution, solution_entities = await self._parse_message_text(
        solution, self.parse_mode
    )
    options = list(
        map(
            lambda opt: PollAnswer(opt, token_bytes(5))
            if isinstance(opt, str)
            else opt,
            options,
        )
    )
    await self.send_file(
        chat_id,
        InputMediaPoll(  # type: ignore
            poll=TypePoll(
                id=0,
                question=question,
                answers=options,
                public_voters=not is_anonymous,
                multiple_choice=multiple_choice,
                closed=closed,
                quiz=quiz,
                close_date=close_date,
            ),
            correct_answers=correct_answers,
            solution=solution,
            solution_entities=solution_entities,
        ),
        schedule=schedule,
    )


async def vote_poll(
    self: TelegramClient, chat_id: "hints.EntityLike", message_id, options
):
    if isinstance(options, int):
        options = [int]
    message: Message = await self.get_messages(chat_id, ids=message_id)  # type: ignore
    if message:
        return await message.click(options)


async def get_users(self: TelegramClient, users):
    if isinstance(users, list):
        return [await self.get_entity(user) for user in users]
    return await self.get_entity(users)


async def set_username(self: TelegramClient, username):
    return await self(UpdateUsernameRequest(username))


async def set_chat_username(self: TelegramClient, chat_id, username):
    return await self(UpdateChatUsername(chat_id, username))


# Patch Pyrogram methods
# setattr(TelegramClient, "get_chat_member", TelegramClient.GetParticipant)  # type: ignore
setattr(TelegramClient, "leave_chat", TelegramClient.delete_dialog)

setattr(TelegramClient, "send_document", send_document)
setattr(TelegramClient, "send_video", send_document)
setattr(TelegramClient, "send_sticker", send_document)
setattr(TelegramClient, "send_voice", send_document)
setattr(TelegramClient, "send_poll", send_poll)
setattr(TelegramClient, "vote_poll", vote_poll)
setattr(TelegramClient, "pin_chat_message", TelegramClient.pin_message)
setattr(TelegramClient, "unpin_chat_message", TelegramClient.unpin_message)

# setattr(TelegramClient, "create_channel", TelegramClient.CreateChannel) # type: ignore

# setattr(TelegramClient, "set_chat_title", TelegramClient.EditTitle) # type: ignore
# setattr(TelegramClient, "get_common_chats", TelegramClient.GetCommonChats) # type: ignore
setattr(TelegramClient, "resolve_peer", TelegramClient.get_input_entity)

# setattr(TelegramClient, "block_user", TelegramClient.Block) # type: ignore
# setattr(TelegramClient, "unblock_user", TelegramClient.Unblock) # type: ignore
setattr(TelegramClient, "set_username", set_username)
setattr(TelegramClient, "set_chat_username", set_chat_username)

setattr(TelegramClient, "get_users", get_users)
setattr(TelegramClient, "get_chat", TelegramClient.get_entity)
setattr(TelegramClient, "run", TelegramClient.run_until_disconnected)

# Message
setattr(Message, "download", Message.download_media)
setattr(Message, "vote", Message.click)
