from aiogram import Dispatcher

from bot import handlers, models
from bot.brains import executor
from bot.config import USE_WEBHOOK, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT


async def on_startup(dp: Dispatcher):
    # models.on_startup(dp)  # TODO: code
    await dp.bot.delete_webhook()
    if USE_WEBHOOK:
        await dp.bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp: Dispatcher):
    pass


def main():
    executor.on_startup(on_startup)
    executor.on_shutdown(on_shutdown)
    if USE_WEBHOOK:
        executor.start_webhook(WEBHOOK_PATH, host=WEBAPP_HOST, port=WEBAPP_PORT)
    else:
        executor.start_polling(reset_webhook=True)


if __name__ == '__main__':
    main()

# TODO: re-check
