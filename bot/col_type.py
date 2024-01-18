from typing import Optional, TypedDict

import discord_types

class EnumType(TypedDict):
    name: str
    value: int

class Channel(TypedDict):
    id: int
    name: str | None
    position: int | None
    nsfw: bool | None
    news: bool | None
    category_id: int | None
    type: EnumType | str | None

class Member(TypedDict):
    id: int
    name: str
    global_name: str | None
    bot: bool
    nick: Optional[str]

class Guild(TypedDict):
    id: int
    name: str
    shard_id: int
    chunked: bool
    member_count: int | None

class Reaction(TypedDict):
    count: int
    emoji_id: int | None
    emoji_name: str | None
    is_custom: bool

class Application(TypedDict):
    id: int
    name: str
    description: str

class Interaction(TypedDict):
    id: int
    name: str
    user_id: int
    type: EnumType | str | None
    created_at: str

class Message(TypedDict):
    id: int
    channel: Channel | None
    author: Member | None
    guild: Guild | None
    content: str
    flags: int
    type: EnumType | str | None
    is_system: bool
    created_at: str
    edited_at: str | None
    attachments: list[discord_types.message.Attachment]
    reactions: list[Reaction]
    embeds: list[discord_types.embed.Embed]
    application: Application | None
    system_content: str
    interaction: Interaction | None

class ClientErrorLog(TypedDict):
    date: str
    time: float
    event_method: str
    args: list
    kwargs: dict
    exc: str

class MessageDeleteLog(TypedDict):
    message_id: int
    channel_id: int
    guild_id: int | None
    bulk: bool

class MemberChangeRoleLog(TypedDict):
    user_id: int
    date: str
    add: list[int]
    remove: list[int]

class MessageEditLog(TypedDict):
    date: str
    channel_id: int
    guild_id: int | None
    message_id: int
    data: dict
