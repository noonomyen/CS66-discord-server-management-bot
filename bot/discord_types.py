from typing import TypedDict, NotRequired, Optional, Union, Any

import discord.types.embed as embed
import discord.types.emoji as emoji
import discord

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

class CustomType_Client(discord.Client):
    def __init__(self, *, intents: discord.flags.Intents, **options: Any) -> None:
        self.command_tree: discord.app_commands.CommandTree
        super().__init__(intents=intents, **options)
