from discord.ext import commands

class DevTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='verbatim', hidden=True)
    @commands.is_owner()
    async def verbatim(self, ctx):
        print(f'verbatim message: {ctx.message.content}')

        verbatim = ctx.message.content.replace('!verbatim', '')
        verbatim = verbatim.replace('<', '<\\')
        await ctx.send(f'{verbatim}')

def setup(bot):
    bot.add_cog(DevTools(bot))
