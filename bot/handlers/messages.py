from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.brain import dp


@dp.message_handler()
async def message_example(message: types.Message, state: FSMContext):
    await message.reply(str(message), reply=False)
