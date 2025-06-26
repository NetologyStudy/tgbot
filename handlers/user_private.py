from aiogram import types, Router, html, F
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


user_private_router = Router()


TEXT = """
/help - помощь для дурачков
/start - запуск жабобота
/bio - жабы
"""


friend_data = {
    "Snezhok_t0p": "CAACAgIAAxkBAAEOyPhoXBFIMnSQlz7siqVxZx84F-4eEgACP3UAArwI4UrmMXyrRmzkbTYE",
    "kreker0k": "CAACAgIAAxkBAAEOyPpoXBGTCR1MhzdVw_mvCOrR5eWMPAACBHkAAtCD4UovOvTf4iGOHjYE",
    "LuciusDeBeers": "CAACAgIAAxkBAAEOyPxoXBGWwLPds0_-52BTHkOzcixKcQACIncAAn_c4Eqa18GjLmcnrTYE",
    "ownllove": "CAACAgIAAxkBAAEOyPRoXBD3zU1wIBOOKueWSutyVKmwfAACPnoAAi5b4Ur777JxLTv8CjYE",
}


FRIEND_INFO = {
    "maxim": {
        "name": "Максим",
        "bio": "Идейный вдохновитель и создатель этого бота. Любит кодить и автоматизировать все подряд.",
        "photo": "https://i.postimg.cc/KvC9bktn/m.jpg"
    },
    "snezhana": {
        "name": "Снежа",
        "bio": "Главный тестриовщик и критик. Находит баги там, где их, казалось бы, нет.",
        "photo": "https://i.postimg.cc/wjKkZKd2/s.jpg"
    },
    "volodya": {
        "name": "Вова",
        "bio": "Моральная поддержка команды!",
        "photo": "https://i.postimg.cc/KvC9bktn/m.jpg"
    },
    "jenya": {
        "name": "Женя",
        "bio": "Моральная поддержка команды!",
        "photo": "https://i.postimg.cc/XJ28zpVB/photo-2025-06-26-16-21-53.jpg"
    },
}


@user_private_router.message(Command("start"))
async def start_command(message: types.Message):
    user_name = message.from_user.username
    full_name = message.from_user.full_name
    sticker_id = friend_data.get(user_name)
    await message.answer(
        f"Привет, {html.bold(full_name)}! 😎",
        parse_mode=ParseMode.HTML)
    if sticker_id:
        await message.answer_sticker(sticker_id)
    else:
        await message.answer(f"Привет, {html.bold(full_name)}! 😎", parse_mode=ParseMode.HTML)


@user_private_router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(TEXT)


@user_private_router.message(Command("bio"))
async def bio(message: types.Message):
    keyboard_builder = InlineKeyboardBuilder()
    for user_id, user_data in FRIEND_INFO.items():
        keyboard_builder.add(InlineKeyboardButton(
            text=user_data['name'],
            callback_data=user_id,
        )
    )
    keyboard_builder.adjust(2)
    await message.answer("О ком хочешь узнать?", reply_markup=keyboard_builder.as_markup())



@user_private_router.callback_query(F.data.in_(FRIEND_INFO))
async def callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.data
    user_data = FRIEND_INFO.get(user_id)
    if user_data:
        await callback.message.answer_photo(
            photo=user_data["photo"],
            caption=f"{html.bold(user_data['name'])}\n{user_data['bio']}",
            parse_mode=ParseMode.HTML,)
