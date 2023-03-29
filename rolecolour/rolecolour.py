from redbot.core import commands, checks
from redbot.core.bot import Red
import discord

class RoleColour(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command('rolecolour', aliases=['rolecolor'])
    @checks.has_permissions(manage_roles=True)
    async def rolecolour(self, ctx: commands.Context, role: discord.Role, colour: discord.Colour):
        await role.edit(colour=colour)
        await ctx.send(f'Role colour changed to {colour}.')