from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):

    # When starting a chat with a bot
    name = State()
    age = State()
    gender = State()
    race = State()

    # In game process
    fight = State()
    chose_attributes = State()
