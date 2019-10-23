import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.utils.executor import Executor

from .config import BOT_TOKEN, SKIP_UPDATES

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
storage = RedisStorage()
dp = Dispatcher(bot, storage=storage)
executor = Executor(dp, skip_updates=SKIP_UPDATES)
