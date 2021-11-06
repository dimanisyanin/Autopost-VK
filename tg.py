from config import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from post import main
import logging
import traceback

logging.basicConfig(level=logging.INFO)

if TOKEN_TG_BOT:
    bot = Bot(token=TOKEN_TG_BOT)
    dp = Dispatcher(bot)