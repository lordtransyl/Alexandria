import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

for cog in ["utility", "moderation", "leveling", "polls", "games"]:
    bot.load_extension(f"cogs.{cog}")

@bot.event
async def on_ready():
    print(f"Bot is ready: {bot.user} (ID: {bot.user.id})")
    print("Ready to run slash commands!")

bot.run(TOKEN)
