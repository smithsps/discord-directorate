from discord.ext import commands
import structlog
import random


class NotSamsFault(commands.Cog):
    total_channel_id = 685711927728799748
    reaction_emoji = [
        '\N{thumbs up sign}',
        '\N{slightly smiling face}',
        '\N{upside-down face}',
        '\N{thinking face}',
        '<:thinkrosa:617807419799633993>',
        '<:danAYAYA:594954949604016147>',
    ]

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='goodsam', hidden=True)
    @commands.guild_only()
    async def not_fault_sam(self, ctx):
        new_total = self.get_total(ctx) + 1
        log.debug('incrementing not sam\'s fault to {new_total}')
        await self.set_total(ctx, new_total)
        await ctx.message.add_reaction(random.choice(self.reaction_emoji))

    @commands.command(name='setnotsamfaults', hidden=True)
    @commands.is_owner()
    async def set_not_sam_faults(self, ctx, total):
        await self.set_total(ctx, total)
        log.debug('setting not sam\'s fault to {new_total}')
        await ctx.message.add_reaction('\N{white heavy check mark}')

    async def set_total(self, ctx, total):
        channel = self.get_channel(ctx)
        await channel.edit(name = f'Not Sam\'s Faults: {total}')

    def get_total(self, ctx):
        channel = self.get_channel(ctx)
        return int(channel.name.split(': ', 1)[1])

    def get_channel(self, ctx):
        return ctx.bot.get_channel(self.total_channel_id)


log = structlog.get_logger()
def setup(bot):
    bot.add_cog(NotSamsFault(bot))
