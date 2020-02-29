import yaml
import discord
from discord.ext import commands

config = yaml.safe_load(open('./settings.yaml'))

def get_prefix(bot, message):
    return commands.when_mentioned_or('!')(bot, message)

initial_extensions = [
    'modules.bens_fault',
    'modules.dev_tools',
]

bot = commands.Bot(command_prefix=get_prefix, description='Authoritator')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {config["version"]}')

    await bot.change_presence(activity=discord.Game(name='GULAG SIM 2000'))
    print(f'\nLogged in and running..!')

bot.run(config['discord-token'], bot=True, reconnect=True)
