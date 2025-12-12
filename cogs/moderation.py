import discord
from discord import app_commands
from discord.ext import commands

ALLOWED_ROLES = ["Admin", "Moderator"]

def is_authorized(interaction: discord.Interaction):
    """Check if user is admin or has an approved role."""
    if interaction.user.guild_permissions.administrator:
        return True

    user_roles = [role.name for role in interaction.user.roles]
    return any(role in ALLOWED_ROLES for role in user_roles)


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Delete messages")
    async def clear(self, interaction: discord.Interaction, amount: int):
        if not is_authorized(interaction):
            return await interaction.response.send_message("❌ You are not authorized.", ephemeral=True)

        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"🧹 Deleted {amount} messages.", ephemeral=True)

    @app_commands.command(name="kick", description="Kick a member")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason"):
        if not is_authorized(interaction):
            return await interaction.response.send_message("❌ You are not authorized.", ephemeral=True)

        await member.kick(reason=reason)
        await interaction.response.send_message(f"👢 Kicked {member.mention}: {reason}")

    @app_commands.command(name="ban", description="Ban a member")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason"):
        if not is_authorized(interaction):
            return await interaction.response.send_message("❌ You are not authorized.", ephemeral=True)

        await member.ban(reason=reason)
        await interaction.response.send_message(f"🔨 Banned {member.mention}: {reason}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
