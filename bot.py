import discord
import yaml

config = yaml.safe_load(open('./settings.yaml'))

def get_prefix(bot, message):
    return commands.when_mentioned_or('!')(bot, message)

initial_extensions = [
    'modules.bens_fault',
]

bot = commands.Bot(command_prefix=get_prefix, description='Authoritator')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n Logged in as: {bot.user.name} - {bot.user.id}\nVersion: {config["version"]}')

    await bot.change_presence(game=discord.Game(name='AUTHORITATE'))
    print(f'Logged in and booted..!')

bot.run(config['discord_token'], bot=True, reconnect=True)
