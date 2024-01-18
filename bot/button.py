from env import CONFIG

import discord
import db

class SelectSection(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Section 01", style=discord.ButtonStyle.primary)
    async def btn_section_01(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user and interaction.guild:
            member = interaction.guild.get_member(interaction.user.id)
            if member:
                db.COL_MCRL.insert_one({
                    "user_id": interaction.user.id,
                    "date": str(interaction.created_at.utcnow()),
                    "add": [CONFIG.ROLE.CS66, CONFIG.ROLE.SECTION_01],
                    "remove": [CONFIG.ROLE.SECTION_02, CONFIG.ROLE.SECTION_03]
                })
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_02))
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_03))
                await member.add_roles(discord.Object(CONFIG.ROLE.CS66))
                await member.add_roles(discord.Object(CONFIG.ROLE.SECTION_01))
                await interaction.response.send_message(content="Section role changed to 01 successful", ephemeral=True)

    @discord.ui.button(label="Section 02", style=discord.ButtonStyle.primary)
    async def btn_section_02(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user and interaction.guild:
            member = interaction.guild.get_member(interaction.user.id)
            if member:
                db.COL_MCRL.insert_one({
                    "user_id": interaction.user.id,
                    "date": str(interaction.created_at.utcnow()),
                    "add": [CONFIG.ROLE.CS66, CONFIG.ROLE.SECTION_02],
                    "remove": [CONFIG.ROLE.SECTION_01, CONFIG.ROLE.SECTION_03]
                })
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_01))
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_03))
                await member.add_roles(discord.Object(CONFIG.ROLE.CS66))
                await member.add_roles(discord.Object(CONFIG.ROLE.SECTION_02))
                await interaction.response.send_message(content="Section role changed to 02 successful", ephemeral=True)

    @discord.ui.button(label="Section 03", style=discord.ButtonStyle.primary)
    async def btn_section_03(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user and interaction.guild:
            member = interaction.guild.get_member(interaction.user.id)
            if member:
                db.COL_MCRL.insert_one({
                    "user_id": interaction.user.id,
                    "date": str(interaction.created_at.utcnow()),
                    "add": [CONFIG.ROLE.CS66, CONFIG.ROLE.SECTION_03],
                    "remove": [CONFIG.ROLE.SECTION_01, CONFIG.ROLE.SECTION_02]
                })
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_01))
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_02))
                await member.add_roles(discord.Object(CONFIG.ROLE.CS66))
                await member.add_roles(discord.Object(CONFIG.ROLE.SECTION_03))
                await interaction.response.send_message(content="Section role changed to 03 successful", ephemeral=True)

    @discord.ui.button(label="Remove", style=discord.ButtonStyle.red)
    async def btn_section_unset(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user and interaction.guild:
            member = interaction.guild.get_member(interaction.user.id)
            if member:
                db.COL_MCRL.insert_one({
                    "user_id": interaction.user.id,
                    "date": str(interaction.created_at.utcnow()),
                    "add": [],
                    "remove": [CONFIG.ROLE.CS66, CONFIG.ROLE.SECTION_01, CONFIG.ROLE.SECTION_02, CONFIG.ROLE.SECTION_03]
                })
                await member.remove_roles(discord.Object(CONFIG.ROLE.CS66))
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_01))
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_02))
                await member.remove_roles(discord.Object(CONFIG.ROLE.SECTION_03))
                await interaction.response.send_message(content="Remove section role successful", ephemeral=True)

class HideSemester(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="2566/1", style=discord.ButtonStyle.primary)
    async def btn_semester_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user and interaction.guild:
            member = interaction.guild.get_member(interaction.user.id)
            if member:
                role = interaction.guild.get_role(CONFIG.ROLE.SS661)
                if role:
                    add: list[int] = []
                    remove: list[int] = []
                    if role in member.roles:
                        remove = [CONFIG.ROLE.SS661]
                        await member.remove_roles(discord.Object(CONFIG.ROLE.SS661))
                        await interaction.response.send_message(content="Remove role successful", ephemeral=True)
                    else:
                        add = [CONFIG.ROLE.SS661]
                        await member.add_roles(discord.Object(CONFIG.ROLE.SS661))
                        await interaction.response.send_message(content="Add role successful", ephemeral=True)
                    db.COL_MCRL.insert_one({
                        "user_id": interaction.user.id,
                        "date": str(interaction.created_at.utcnow()),
                        "add": add,
                        "remove": remove
                    })

    @discord.ui.button(label="2566/2", style=discord.ButtonStyle.primary)
    async def btn_semester_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user and interaction.guild:
            member = interaction.guild.get_member(interaction.user.id)
            if member:
                role = interaction.guild.get_role(CONFIG.ROLE.SS662)
                if role:
                    add: list[int] = []
                    remove: list[int] = []
                    if role in member.roles:
                        remove = [CONFIG.ROLE.SS662]
                        await member.remove_roles(discord.Object(CONFIG.ROLE.SS662))
                        await interaction.response.send_message(content="Remove role successful", ephemeral=True)
                    else:
                        add = [CONFIG.ROLE.SS662]
                        await member.add_roles(discord.Object(CONFIG.ROLE.SS662))
                        await interaction.response.send_message(content="Add role successful", ephemeral=True)
                    db.COL_MCRL.insert_one({
                        "user_id": interaction.user.id,
                        "date": str(interaction.created_at.utcnow()),
                        "add": add,
                        "remove": remove
                    })
