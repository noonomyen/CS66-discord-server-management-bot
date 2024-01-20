from env import CONFIG
from discord import app_commands
from discord.app_commands import Choice

import discord
import button
import db
import obj2dict
import modal

def load_command_tree(tree: app_commands.CommandTree, guild_id: int) -> None:
    @tree.command(name="button-give-role", description="Manage buttons in #give-role channel", guild=discord.Object(guild_id))
    @app_commands.describe(action="action")
    @app_commands.choices(action=[Choice(name="send", value=1), Choice(name="purge", value=2)])
    async def button_give_role(interaction: discord.Interaction, action: Choice[int]):
        accept = False
        if isinstance(interaction.user, discord.Member):
            if interaction.user.guild_permissions.administrator:
                accept = True
            else:
                await interaction.response.send_message(content="This command is for administrators only", ephemeral=True)
                return

        db.COL_ACL.insert_one({
            "date": str(interaction.created_at.utcnow()),
            "guild_id": interaction.guild_id,
            "channel_id": interaction.channel_id,
            "interaction_id": interaction.id,
            "user_id": interaction.user.id,
            "data": {
                "name": "button-give-role",
                "action": obj2dict.Enum2Dict(action)
            },
            "accept": accept
        })

        if accept and interaction.guild:
            role_channel = interaction.guild.get_channel(CONFIG.CHANNEL.ROLE)
            if role_channel and not isinstance(role_channel, (discord.ForumChannel, discord.CategoryChannel)):
                if action.value == 1:
                    await role_channel.send("# Press the button to get role")
                    await role_channel.send(content="## Class section", view=button.SelectSectionView())
                    await role_channel.send(content="## Semester (Hide category)", view=button.HideSemesterView())
                    await interaction.response.send_message(content="Successful", ephemeral=False if interaction.channel_id == CONFIG.CHANNEL.DSMB else True)
                elif action.value == 2:
                    await role_channel.purge()
                    await interaction.response.send_message(content="Purged", ephemeral=False if interaction.channel_id == CONFIG.CHANNEL.DSMB else True)
                else:
                    await interaction.response.send_message(content="Argument error", ephemeral=False if interaction.channel_id == CONFIG.CHANNEL.DSMB else True)

    @tree.command(name="send-message", description="Send message in this channel with bot", guild=discord.Object(guild_id))
    async def send_message(interaction: discord.Interaction):
        accept = False
        if isinstance(interaction.user, discord.Member):
            if interaction.user.guild_permissions.administrator:
                accept = True
            else:
                await interaction.response.send_message(content="This command is for administrators only", ephemeral=True)
                return

        db_result = db.COL_ACL.insert_one({
            "date": str(interaction.created_at.utcnow()),
            "guild_id": interaction.guild_id,
            "channel_id": interaction.channel_id,
            "interaction_id": interaction.id,
            "user_id": interaction.user.id,
            "data": {
                "name": "send-message",
                "message": None
            },
            "accept": accept
        })

        if accept and interaction.channel_id and isinstance(interaction.user, discord.Member):
            await interaction.response.send_modal(modal.SendMessage_TextInput(interaction.channel_id, interaction.user.id, db_result.inserted_id))
        else:
            await interaction.response.send_message(content="Failed", ephemeral=True)
