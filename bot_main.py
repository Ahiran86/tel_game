import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.start import router as start_router
from bot.help import router as help_router

from core.config import settings

print("this file started")
async def main():
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(help_router)

    await dp.start_polling(bot)


asyncio.run(main())