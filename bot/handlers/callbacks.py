from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.brain import dp


@dp.message_handler(commands=['start', 'help'])
async def callback_example(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
