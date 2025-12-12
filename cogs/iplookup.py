import discord
from discord import app_commands
from discord.ext import commands
import requests

class IPLookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="iplookup", description="Lookup information about an IP address")
    async def iplookup(self, interaction: discord.Interaction, ip: str):
        url = f"http://ip-api.com/json/{ip}"
        res = requests.get(url).json()

        if res["status"] != "success":
            return await interaction.response.send_message("❌ Invalid IP address.")

        embed = discord.Embed(title=f"🌍 IP Lookup: {ip}", color=discord.Color.green())
        embed.add_field(name="Country", value=res.get("country"))
        embed.add_field(name="City", value=res.get("city"))
        embed.add_field(name="ISP", value=res.get("isp"))
        embed.add_field(name="Lat/Lon", value=f"{res.get('lat')}, {res.get('lon')}")
        embed.add_field(name="Timezone", value=res.get("timezone"))
        embed.set_footer(text="Powered by ip-api.com (free API)")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(IPLookup(bot))
