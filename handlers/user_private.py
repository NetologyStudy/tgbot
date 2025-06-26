from aiogram import types, Router, html
from aiogram.enums import ParseMode
from aiogram.filters.command import Command


user_private_router = Router()


TEXT = """
/help - помощь для дурачков
/start - запуск жабобота
"""


@user_private_router.message(Command("start"))
async def start_command(message: types.Message):
    if message.from_user.username == "Snezhok_t0p":
        await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! 😎", parse_mode=ParseMode.HTML)
        await message.answer_sticker("CAACAgIAAxkBAAEOyPhoXBFIMnSQlz7siqVxZx84F-4eEgACP3UAArwI4UrmMXyrRmzkbTYE")
    elif message.from_user.username == "kreker0k":
        await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! 😎", parse_mode=ParseMode.HTML)
        await message.answer_sticker("CAACAgIAAxkBAAEOyPpoXBGTCR1MhzdVw_mvCOrR5eWMPAACBHkAAtCD4UovOvTf4iGOHjYE")
    elif message.from_user.username == "LuciusDeBeers":
        await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! 😎", parse_mode=ParseMode.HTML)
        await message.answer_sticker("CAACAgIAAxkBAAEOyPxoXBGWwLPds0_-52BTHkOzcixKcQACIncAAn_c4Eqa18GjLmcnrTYE")
    elif message.from_user.username == "ownllove":
        await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! 😎", parse_mode=ParseMode.HTML)
        await message.answer_sticker("CAACAgIAAxkBAAEOyPRoXBD3zU1wIBOOKueWSutyVKmwfAACPnoAAi5b4Ur777JxLTv8CjYE")


@user_private_router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(TEXT)


@user_private_router.message(Command("about"))
async def help_command(message: types.Message):
    await message.answer("О нас:")