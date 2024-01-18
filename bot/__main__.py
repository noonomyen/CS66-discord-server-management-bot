from asyncio import tasks
from env import CONFIG
from typing import Any
from traceback import format_exc
from datetime import datetime
from discord.ext import tasks

import discord
import db
import col_type
import obj2dict
import button

class Client(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.all()
        options = {
            "max_messages": None
        }

        super().__init__(intents=intents, **options)

    async def on_ready(self) -> None:
        print("Logged on as", self.user)
        await self.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=CONFIG.VERSION)
        )
        self.auto_send_message_button_give_role.start()

    async def on_message(self, message: discord.Message) -> None:
        if message.channel.id != CONFIG.CHANNEL.DELETE_LOG:
            db.COL_ML.insert_one(obj2dict.MessageObj2Dict(message))

    async def on_raw_message_delete(self, payload: discord.RawMessageDeleteEvent) -> None:
        if payload.guild_id == CONFIG.GUILD_ID:
            dt = datetime.now()
            db.COL_MDL.insert_one({
                "message_id": payload.message_id,
                "channel_id": payload.channel_id,
                "guild_id": payload.guild_id,
                "bulk": False
            })
            if payload.guild_id:
                guild = self.get_guild(payload.guild_id)
                if guild:
                    channel = guild.get_channel(CONFIG.CHANNEL.DELETE_LOG)
                    if channel:
                        message = db.COL_ML.find_one({ "id": payload.message_id })
                        if message:
                            await channel.send(f"[{dt.utcnow()}] MESSAGE_DELETE AUTHOR_ID:`{message['author']['id']}` MESSAGE_ID:`{message['id']}` CONTENT:`{repr(message['content'])}`") # type: ignore
                        else:
                            raise Exception(f"Message ID not found {payload.message_id} in database")
                    else:
                        raise Exception("'channel' is None")
                else:
                    raise Exception("'guild' is None")

    async def on_raw_bulk_message_delete(self, payload: discord.RawBulkMessageDeleteEvent) -> None:
        if payload.guild_id == CONFIG.GUILD_ID:
            dt = datetime.now()
            list_: list[col_type.MessageDeleteLog] = []
            for id in payload.message_ids:
                list_.append({
                    "message_id": id,
                    "channel_id": payload.channel_id,
                    "guild_id": payload.guild_id,
                    "bulk": True
                })
            db.COL_MDL.insert_many(list_)
            if payload.guild_id:
                guild = self.get_guild(payload.guild_id)
                if guild:
                    channel = guild.get_channel(CONFIG.CHANNEL.DELETE_LOG)
                    if channel:
                        await channel.send(f"[{dt.utcnow()}] BULK_MESSAGE_DELETE ID_LIST:`{','.join([str(x['message_id']) for x in list_])}`") # type: ignore
                    else:
                        raise Exception("'channel' is None")
                else:
                    raise Exception("'guild' is None")

    async def on_raw_message_edit(self, payload: discord.RawMessageUpdateEvent) -> None:
        dt = datetime.now()
        db.COL_MEL.insert_one({
            "date": str(dt.utcnow()),
            "guild_id": payload.guild_id,
            "channel_id": payload.channel_id,
            "message_id": payload.message_id,
            "data": obj2dict.FilterDict(payload.data)
        })

    async def on_error(self, event_method: str, /, *args: Any, **kwargs: Any) -> None:
        dt = datetime.now()
        db.COL_CEL.insert_one({
            "date": str(dt.utcnow()),
            "time": dt.timestamp(),
            "event_method": event_method,
            "args": obj2dict.FilterList(args),
            "kwargs": obj2dict.FilterDict(kwargs),
            "exc": format_exc()
        })
        await super().on_error(event_method, *args, **kwargs)

    @tasks.loop(seconds=CONFIG.AUTO_SEND_MEESAGE_BUTTON_GIVE_ROLE)
    async def auto_send_message_button_give_role(self):
        guild = self.get_guild(CONFIG.GUILD_ID)
        if guild:
            channel = guild.get_channel(CONFIG.CHANNEL.ROLE)
            if channel and not isinstance(channel, (discord.ForumChannel, discord.CategoryChannel)):
                await channel.purge()
                await channel.send("# Press the button to get role")
                await channel.send(content="## Class section", view=button.SelectSection())
                await channel.send(content="## Semester (Hide category)", view=button.HideSemester())

Client().run(CONFIG.TOKEN)
