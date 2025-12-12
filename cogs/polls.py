import discord
from discord import app_commands
from discord.ext import commands

class Polls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="poll", description="Create a poll with reactions")
    async def poll(self, interaction: discord.Interaction, question: str, option1: str, option2: str):
        embed = discord.Embed(
            title="📊 Poll",
            description=f"**{question}**\n\n1️⃣ {option1}\n2️⃣ {option2}",
            color=discord.Color.blue()
        )

        msg = await interaction.channel.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")

        await interaction.response.send_message("Poll created!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Polls(bot))
