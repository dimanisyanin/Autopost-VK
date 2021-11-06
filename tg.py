import subprocess

from config import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from post import main
import logging
import traceback
from core import post

logging.basicConfig(level=logging.INFO)

if TOKEN_TG_BOT:
    bot = Bot(token=TOKEN_TG_BOT)
    dp = Dispatcher(bot)
    code = """
from config import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from post import main
import logging
import traceback
from core import post
bot = Bot(token=TOKEN_TG_BOT)
dp = Dispatcher(bot)

async def on_startup(q):
    while True:
        await bot.send_message(TG_ID, str(post.posts()))

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
    """
else:
    code = "post.posts()"

proc = subprocess.run(
    ['python3', '-c', code]
)

#@dp.message_handler()
#async def error_msg():
#    await bot.send_message(TG_ID, str(post.posts()))

#if __name__ == '__main__':
#    executor.start_polling(dp)