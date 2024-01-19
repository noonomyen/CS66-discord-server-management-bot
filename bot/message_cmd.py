from discord_types import CustomType_Client

import discord
import db

help_command = "```"
help_command += "sync-command-tree -- Syncs the application commands to this server"
help_command += "```"

async def message_commnad(client: CustomType_Client, message: discord.Message):
    accept = False
    if isinstance(message.author, discord.Member):
        if message.author.guild_permissions.administrator:
            accept = True
        else:
            await message.reply("This command is for administrators only")
            return

    db.COL_MCL.insert_one({
        "date": str(message.created_at.utcnow()),
        "guild_id": message.guild.id if message.guild else None,
        "channel_id": message.channel.id,
        "message_id": message.id,
        "user_id": message.author.id,
        "accept": accept
    })

    cmd = message.content.split()
    cmd_len = len(cmd)

    if cmd_len == 1 or (cmd_len == 2 and cmd[1] == "--help"):
        await message.channel.send(help_command)
    else:
        if cmd_len == 2 and (cmd[1] == "sync-command-tree") and message.guild:
            await client.command_tree.sync(guild=discord.Object(message.guild.id))
            await message.reply("Synced")
        else:
            await message.reply(f"Unknown command '{repr(cmd[1])}'")
