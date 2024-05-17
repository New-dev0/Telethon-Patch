import hashlib
from telethon.tl import types
from telethon.tl.custom import InlineBuilder


async def article(
    self: "InlineBuilder",
    title,
    description=None,
    *,
    url=None,
    thumb=None,
    content=None,
    id=None,
    text=None,
    parse_mode=(),
    link_preview=True,
    geo=None,
    period=60,
    contact=None,
    game=False,
    buttons=None,
    type="article",
    include_media: bool = False
):
    """
    Creates new inline result of article type.

    Args:
        title (`str`):
            The title to be shown for this result.

        description (`str`, optional):
            Further explanation of what this result means.

        url (`str`, optional):
            The URL to be shown for this result.

        thumb (:tl:`InputWebDocument`, optional):
            The thumbnail to be shown for this result.
            For now it has to be a :tl:`InputWebDocument` if present.

        content (:tl:`InputWebDocument`, optional):
            The content to be shown for this result.
            For now it has to be a :tl:`InputWebDocument` if present.

    Example:
        .. code-block:: python

            results = [
                # Option with title and description sending a message.
                builder.article(
                    title='First option',
                    description='This is the first option',
                    text='Text sent after clicking this option',
                ),
                # Option with title URL to be opened when clicked.
                builder.article(
                    title='Second option',
                    url='https://example.com',
                    text='Text sent if the user clicks the option and not the URL',
                ),
                # Sending a message with buttons.
                # You can use a list or a list of lists to include more buttons.
                builder.article(
                    title='Third option',
                    text='Text sent with buttons below',
                    buttons=Button.url('https://example.com'),
                ),
            ]
    """
    # TODO Does 'article' work always?
    # article, photo, gif, mpeg4_gif, video, audio,
    # voice, document, location, venue, contact, game
    result = types.InputBotInlineResult(
        id=id or "",
        type=type,
        send_message=await self._message(
            text=text,
            parse_mode=parse_mode,
            link_preview=link_preview,
            geo=geo,
            period=period,
            contact=contact,
            game=game,
            buttons=buttons,
            media=include_media
        ),
        title=title,
        description=description,
        url=url,
        thumb=thumb,
        content=content,
    )
    if id is None:
        result.id = hashlib.sha256(bytes(result)).hexdigest()

    return result

setattr(InlineBuilder, "article", article)