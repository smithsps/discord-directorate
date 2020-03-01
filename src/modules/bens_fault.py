from discord.ext import commands
import structlog
import random


class BensFault(commands.Cog):
    total_channel_id = 630157407955451925
    reaction_emoji = [
        '\N{white heavy check mark}',
        '\N{ok hand sign}',
        '\N{thumbs up sign}',
        '\N{rolling on the floor laughing}',
        '\N{slightly smiling face}',
        '\N{upside-down face}',
        '<:thinkrosa:617807419799633993>',
        '<:sydneychan:595469748758904843>',
    ]

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='faultben', hidden=True)
    @commands.guild_only()
    async def fault_ben(self, ctx):
        new_total = self.get_total(ctx) + 1
        log.debug('incrementing ben\'s fault to {new_total}')
        await self.set_total(ctx, new_total)
        await ctx.message.add_reaction(random.choice(self.reaction_emoji))

    @commands.command(name='setbenfaults', hidden=True)
    @commands.is_owner()
    async def set_faults(self, ctx, total):
        await self.set_total(ctx, total)
        log.debug('setting ben\'s fault to {new_total}')
        await ctx.message.add_reaction('\N{white heavy check mark}')

    async def set_total(self, ctx, total):
        channel = self.get_channel(ctx)
        await channel.edit(name = f'Ben\'s Faults: {total}')

    def get_total(self, ctx):
        channel = self.get_channel(ctx)
        return int(channel.name.split(': ', 1)[1])

    def get_channel(self, ctx):
        return ctx.bot.get_channel(self.total_channel_id)


log = structlog.get_logger()
def setup(bot):
    bot.add_cog(BensFault(bot))
