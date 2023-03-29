from redbot.core.bot import Red

from .rolecolour import RoleColour

async def setup(bot: Red):
    bot.add_cog(RoleColour(bot))