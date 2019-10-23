from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):

    # When starting a chat with a bot
    example = State()
