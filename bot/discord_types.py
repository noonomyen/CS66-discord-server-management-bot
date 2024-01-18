from typing import TypedDict, NotRequired, Optional, Union

import discord.types.embed as embed
import discord.types.emoji as emoji

class message:
    class Attachment(TypedDict):
        id: Union[str, int]
        filename: str
        size: int
        url: str
        proxy_url: str
        height: NotRequired[Optional[int]]
        width: NotRequired[Optional[int]]
        description: NotRequired[str]
        content_type: NotRequired[str]
        spoiler: NotRequired[bool]
        ephemeral: NotRequired[bool]
        duration_secs: NotRequired[float]
        waveform: NotRequired[str]
