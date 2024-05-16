from telethon.tl.custom import Message as BaseMessage

class Message(
    BaseMessage
):
    download = BaseMessage.download_media
    vote = BaseMessage.click
    
    @property
    def message_link(self):
        if hasattr(self.chat, "username") and self.chat.username:
            return f"https://t.me/{self.chat.username}/{self.id}"
        if (self.chat and self.chat.id):
            chat = self.chat.id
        elif self.chat_id:
            if str(self.chat_id).startswith("-" or "-100"):
                chat = int(str(self.chat_id).replace("-100", "").replace("-", ""))
            else:
                chat = self.chat_id
        else:
            return
        return f"https://t.me/c/{chat}/{self.id}"
