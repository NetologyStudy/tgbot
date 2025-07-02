import asyncio
from aiogram import Bot, Dispatcher, types

from config import settings

from handlers.user_private import user_private_router as upr
from handlers.reminder_hundlers import reminder_router as ru
from common.bot_cmds_llist import private


async def main():
    bot = Bot(token=settings.API_TOKEN)
    dp = Dispatcher()

    dp.include_routers(upr, ru)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
