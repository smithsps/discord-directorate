from discord.ext import commands
import structlog
from types import SimpleNamespace

class ColorRoles(commands.Cog):
    possible_roles = [
        (684179818790912010, 'teal'),
        (684179830841147396, 'green'),
        (684179832141381674, 'blue'),
        (684179833168986119, 'purple'),
        (684179834477477929, 'pink'),
        (684179974718095381, 'gold'),
        (684179976731361281, 'orange'),
        (684179977603907712, 'peach'),
        (684180639645565010, 'red'),
        (0, 'none'),
    ]

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rolecolor', hidden=True)
    async def rolecolor(self, ctx, color):
        color_role = next((cr for cr in self.possible_roles if cr[1] == color.lower()), None)
        if color_role is None:
            await ctx.send(f'Available colors are: {self.listed_colors()}')
            return

        # Remove current color roles
        current_roles = ctx.author.roles
        for color in self.possible_roles:
            if color[0] in [r.id for r in current_roles]:
                role = SimpleNamespace(id=color[0])
                await ctx.author.remove_roles(role)

        if (color_role[1] == 'none'):
            return

        role = SimpleNamespace(id=color_role[0])
        await ctx.author.add_roles(role)
        await ctx.message.add_reaction('\N{white heavy check mark}')

    @rolecolor.error
    async def rolecolor_error(self, ctx, error):
        if isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'\!rolecolor <color>\nAvailable colors are: {self.listed_colors()}')
        else:
            log.error(error)

    def listed_colors(self):
        return ', '.join([r[1] for r in self.possible_roles])


log = structlog.get_logger()
def setup(bot):
    bot.add_cog(ColorRoles(bot))
