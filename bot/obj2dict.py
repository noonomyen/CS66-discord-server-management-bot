import col_type
import discord_types
import discord

def MessageObj2Dict(message: discord.Message) -> col_type.Message:
    message_channel: col_type.Channel | None = None
    if message.channel:
        message_channel = {
            "id": message.channel.id,
            "name": message.channel.name if not isinstance(message.channel, (discord.DMChannel, discord.PartialMessageable)) else None,
            "position": message.channel.position if not isinstance(message.channel, (discord.Thread, discord.GroupChannel, discord.DMChannel, discord.PartialMessageable)) else None,
            "nsfw": message.channel.nsfw if not isinstance(message.channel, (discord.Thread, discord.GroupChannel, discord.DMChannel, discord.PartialMessageable)) else None,
            "news": message.channel.is_news() if not isinstance(message.channel, (discord.VoiceChannel, discord.StageChannel, discord.GroupChannel, discord.DMChannel, discord.PartialMessageable)) else None,
            "category_id": message.channel.category_id if not isinstance(message.channel, (discord.GroupChannel, discord.DMChannel, discord.PartialMessageable)) else None,
            "type": Enum2Dict(message.channel.type)
        }

    message_author: col_type.Member | None = None
    if message.author:
        message_author = {
            "id": message.author.id,
            "name": message.author.name,
            "global_name": message.author.global_name,
            "bot": message.author.bot,
            "nick": message.author.nick if isinstance(message.author, discord.Member) else None
        }

    message_guild: col_type.Guild | None = None
    if message.guild:
        message_guild = {
            "id": message.guild.id,
            "name": message.guild.name,
            "shard_id": message.guild.shard_id,
            "chunked": message.guild.chunked,
            "member_count": message.guild.member_count
        }

    message_attachments: list[discord_types.message.Attachment] = []
    for attachment in message.attachments:
        message_attachments.append(attachment.to_dict())

    message_reaction: list[col_type.Reaction] = []
    for reaction in message.reactions:
        emoji_id: int | None = None
        emoji_name: str | None = None
        if isinstance(reaction.emoji, (discord.PartialEmoji, discord.Emoji)):
            emoji_id = reaction.emoji.id
            emoji_name = reaction.emoji.name

        message_reaction.append({
            "count": reaction.count,
            "emoji_id": emoji_id,
            "emoji_name": emoji_name,
            "is_custom": reaction.is_custom_emoji()
        })

    message_embeds: list[discord_types.embed.Embed] = []
    for embed in message.embeds:
        message_embeds.append(embed.to_dict())

    message_application: col_type.Application | None = None
    if message.application:
        message_application = {
            "id": message.application.id,
            "name": message.application.name,
            "description": message.application.description
        }

    message_interaction: col_type.Interaction | None = None
    if message.interaction:
        message_interaction = {
            "id": message.interaction.id,
            "name": message.interaction.name,
            "created_at": str(message.interaction.created_at.utcnow()),
            "type": Enum2Dict(message.interaction.type),
            "user_id": message.interaction.user.id
        }

    obj: col_type.Message = {
        "id": message.id,
        "channel": message_channel,
        "author": message_author,
        "guild": message_guild,
        "content": message.content,
        "flags": message.flags.value,
        "type": Enum2Dict(message.type),
        "created_at": str(message.created_at.utcnow()),
        "edited_at": str(message.edited_at.utcnow()) if message.edited_at else None,
        "is_system": message.is_system(),
        "attachments": message_attachments,
        "reactions": message_reaction,
        "embeds": message_embeds,
        "application": message_application,
        "system_content": message.system_content,
        "interaction": message_interaction
    }

    return obj

def FilterList(data) -> list:
    new_list = []
    for element in data:
        if type(element) in (int, float, str, bool):
            new_list.append(element)
        elif type(element) in (list, tuple, set, frozenset):
            new_list.append(FilterList(list(element)))
        elif type(element) == dict:
            new_list.append(FilterDict(element))
        else:
            new_list.append(element)

    return new_list

def FilterDict(data) -> dict:
    new_dict = {}
    for key, value in data.items():
        if type(value) in [int, float, str, bool]:
            new_dict[key] = value
        elif type(value) in (list, tuple, set, frozenset):
            new_dict[key] = FilterList(list(value))
        elif type(value) == dict:
            new_dict[key] = FilterDict(value)
        else:
            new_dict[key] = value

    return new_dict

def Enum2Dict(enum) -> col_type.EnumType | str | None:
    if hasattr(enum, "name") and hasattr(enum, "value"):
        return { "name": enum.name, "value": enum.value }
    elif enum != None:
        return str(enum)
    else:
        return None
