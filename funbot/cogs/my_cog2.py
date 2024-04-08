from discord.ext import commands
from funbot.utils.helpers import get_formatted_name

class AnotherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='greet')
    async def greet(self, ctx, *, name: str = None):
        """Greets a user."""
        name = name or 'there'
        formatted_name = get_formatted_name(name)
        await ctx.send(f'Hello {formatted_name}!')

def setup(bot):
    bot.add_cog(AnotherCog(bot))