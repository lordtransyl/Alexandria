import discord
from discord import app_commands
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! {round(self.bot.latency*1000)}ms")

    @app_commands.command(name="coin", description="Flip a coin")
    async def coin(self, interaction: discord.Interaction):
        import random
        result = random.choice(["Heads", "Tails"])
        await interaction.response.send_message(f"🪙 {result}")

async def setup(bot):
    await bot.add_cog(Utility(bot))
