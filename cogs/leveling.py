import discord
from discord import app_commands
from discord.ext import commands
import aiosqlite
import random


def get_evolution_stage(level):
    if level <= 10:
        return "🪶 Initiate Scribe"
    elif level <= 20:
        return "📜 Arcane Scholar"
    elif level <= 35:
        return "🔮 Mystic Archivist"
    elif level <= 50:
        return "🗝️ Grand Curator"
    else:
        return "🔱 Keeper of the Vault"


class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.setup_db())

    async def setup_db(self):
        self.db = await aiosqlite.connect("levels.db")
        await self.db.execute(
            "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, xp INTEGER, level INTEGER)"
        )
        await self.db.commit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        xp_gain = random.randint(5, 15)

        async with self.db.execute("SELECT xp, level FROM users WHERE user_id = ?", (message.author.id,)) as cursor:
            row = await cursor.fetchone()

        if row is None:
            await self.db.execute(
                "INSERT INTO users VALUES (?, ?, ?)",
                (message.author.id, xp_gain, 1)
            )
            await self.db.commit()
            return

        xp, level = row
        xp += xp_gain

        level_up = False
        while xp >= level * 100:
            xp -= level * 100
            level += 1
            level_up = True

        await self.db.execute(
            "UPDATE users SET xp = ?, level = ? WHERE user_id = ?",
            (xp, level, message.author.id),
        )
        await self.db.commit()

        if level_up:
            stage = get_evolution_stage(level)
            await message.channel.send(
                f"🎉 {message.author.mention} reached **Level {level}!**\n"
                f"🌟 **Evolution Stage:** {stage}"
            )

    @app_commands.command(name="rank", description="Check your level and evolution stage")
    async def rank(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user

        async with self.db.execute("SELECT xp, level FROM users WHERE user_id = ?", (member.id,)) as cursor:
            row = await cursor.fetchone()

        if row is None:
            return await interaction.response.send_message("No data found for this user.")

        xp, level = row
        stage = get_evolution_stage(level)

        embed = discord.Embed(
            title=f"{member.name}'s Rank",
            color=discord.Color.purple()
        )
        embed.add_field(name="Level", value=level)
        embed.add_field(name="XP", value=f"{xp} / {level * 100}")
        embed.add_field(name="Evolution Stage", value=stage)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Leveling(bot))
