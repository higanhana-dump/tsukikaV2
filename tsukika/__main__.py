import logging
import sys
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s", stream=sys.stdout)

from tsukika.bot import tsukikaBrain
from tsukika import tsukikaConfig
bot = tsukikaBrain.create()
bot.run(tsukikaConfig.DISCORD_TOKEN)