import discord
import discord.ui
import db

class SendMessage_TextInput(discord.ui.Modal):
    message = discord.ui.TextInput(label="Message", style=discord.TextStyle.paragraph, required=True, max_length=2000)

    def __init__(self, channel_id: int, user_id: int, db_inserted_id: int) -> None:
        self.db_inserted_id = db_inserted_id
        self.channel_id = channel_id
        self.user_id = user_id
        super().__init__(title="Send message (bot)", timeout=120)

    async def on_submit(self, interaction: discord.Interaction):
        db.COL_ACL.update_one({ "_id": self.db_inserted_id }, { "$set": { "data": { "name": "send-message", "message": self.message.value } } })
        if interaction.guild:
            channel = interaction.guild.get_channel(self.channel_id)
            await channel.send(content=self.message.value) # type: ignore
        await interaction.response.send_message("Successful", ephemeral=True)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return isinstance(interaction.user, discord.Member) and self.user_id == interaction.user.id;
