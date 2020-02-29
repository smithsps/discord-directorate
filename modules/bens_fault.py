from discord.ext import commands

class BensFaultCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.total_channel_id = 630157407955451925
        self.reaction_emoji = ':white_check_mark:'

    @commands.command(name='fault_ben', hidden=True)
    @command.guild_only()
    async def fault_ben(self, ctx):
        print('bensfault!')

        ctx.message.add_reaction(self.reaction_emoji)

    @commands.command(name='set_faults', hidden=True)
    @command.is_owner()
    async def set_faults(self, ctx, faults):
        print(f'setting bens faults to {faults}!')

        ctx.message.add_reaction(self.reaction_emoji)

def setup(bot):
    bot.add_cog(BensFaultCog(bot))
