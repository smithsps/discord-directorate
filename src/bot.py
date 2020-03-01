import discord
from discord.ext import commands
import logging
import structlog
import sys
import yaml

config = yaml.safe_load(open('./settings.yaml'))

logging.basicConfig(
    format="%(message)s", stream=sys.stdout, level=logging.INFO
)

structlog.configure(
    logger_factory=structlog.stdlib.LoggerFactory(),
)

log = structlog.get_logger()

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
    log.info(f'\nLogged in as: {bot.user.name} - {bot.user.id} - V.{config["version"]}')

    await bot.change_presence(activity=discord.Game(name='GULAG SIM 2000'))
    log.info(f'\nLogged in and running..!')

bot.run(config['discord-token'], bot=True, reconnect=True)
