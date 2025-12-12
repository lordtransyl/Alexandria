import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

COGS = [
    "utility",
    "moderation",
    "leveling",
    "polls",
    "games",
    "iplookup"
]

# Load cogs properly (ASYNC)
async def load_cogs():
    for cog in COGS:
        await bot.load_extension(f"cogs.{cog}")
        print(f"Loaded cog: {cog}")

@bot.event
async def on_ready():
    print(f"Bot is ready: {bot.user} (ID: {bot.user.id})")
    await bot.tree.sync()
    print("Ready to run slash commands!")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

# Start bot
asyncio.run(main())
