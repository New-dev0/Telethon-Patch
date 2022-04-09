# Telethon-Patch
- A Wrap over Telethon (Telegram MtProto Library), providing Layer 139 and additional features.

## Installation
```bash
pip install telethon-patch
```
* (Make Sure, Telethon is not already installed on your system, `telethon-patch` will do that for you!)

### Usage
- To make telethon-patch to do it's work, add this lines before creating TelegramClient
```python
from telethonpatch import apply
apply()
```

## Features
#### Use any Function without Import
```python
await client.SendReactionRequest("chat", msg.id, reaction="👍")
# or (Without 'Request' prefix)
await client.SendReaction(chat, msg.id, reaction="👍")
```

### Send Button linked to User's profile
```python
from telethon.tl.types import Button

user = await client.get_input_entity("me")
button = Button.mention("Open Profile", user)

await client.send_message("username", "Hey!, Message with mention Button", buttons=button)
```

### Chat Join Requests ([In Detail](#eventsjoinrequest))
```python
from telethon import events

@client.on(events.JoinRequest())
async def example(event):
    ## Approve - User
    await event.approve()
    ## Disapprove user
    await event.reject()
    # or print Info of the user.
    print(await event.get_user())
```

### Group Call Event ([In Detail](#eventsgroupcall))
```python
@client.on(events.GroupCall())
async def groupcall(group_call):
    if group_call.started:
        print("Group Call Started!")
        return
    if group_call.ended:
        print("Group Call Ended!")
```

### Message Extensions
- `message.message_link` - `Message link of message.`
- `message.comment()` - Bound method to comment on channel or thread message.
- `message.react()` - Bound method to react on messages.


### Friendly Methods like
 > client.start_group_call

 > client.read (instead of send_read_acknowledge)


# Events

## `events.GroupCall`
- Occurs when certain action related to group call happens.
-  `started` - Group call started.
-  `ended` - Group call ended.
-  `scheduled` - Whether a Group call has been scheduled.

#### Methods
- `.start(title, rtmp_stream, schedule)` - Start a group call
- `.discard()` - End group call.
- `.toggle_record(start, video, video_portrait, title)` - Toggle group call record.

## `events.JoinRequest`
- Occurs when new chat join request is sent.
- `.invite` - ExportedChatInvite related to join request
- `.about` - User's about.

#### Methods
- `.approve()` - Approve chat join request of user.
- `.reject()` - Reject chat join request.
- `.get_user()` - Get user sending request.

### Example of full functioning bot can be find in [examples](/examples)