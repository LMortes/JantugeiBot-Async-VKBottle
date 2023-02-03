import db_connect
from loguru import logger
from handlers import labelers
import asyncio
from settings import bot, labeler
global conn


logger.disable("vkbottle")
bot.labeler.vbml_ignore_case = True

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)



async def start(loop):
    await db_connect.connection(loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start(loop))
    print('Бот успешно запущен')
    bot.run_forever()

