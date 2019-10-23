from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.brain import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply("Да?", reply=False)
