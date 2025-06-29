from aiogram import types, Router, html, F
from aiogram.enums import ParseMode
from aiogram.filters import or_f
from aiogram.filters.command import Command, CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline import get_friends_keyboard, CALLBACK_BACK_TO_MAIN

from user_info import  FRIEND_DATA, FRIEND_INFO

user_private_router = Router()


TEXT = """
/start - запуск жабобота
/help - помощь для дурачков
/bio - жабы
"""


@user_private_router.message(CommandStart())
async def start_command(message: types.Message):
    user_name = message.from_user.username
    full_name = message.from_user.full_name
    sticker_id = FRIEND_DATA.get(user_name)
    await message.answer(
        f"""
        Привет, {html.bold(full_name)}! Я помогу тебе использовать свободное время с пользой!
           
Что я могу:
        
/bio - Информация о наших жабах
        """,
        parse_mode=ParseMode.HTML,
    )

    if sticker_id:
        await message.answer_sticker(sticker_id)
    else:
        await message.answer(f"Привет, {html.bold(full_name)}! 😎", parse_mode=ParseMode.HTML)


@user_private_router.message(or_f(Command("bio"), (F.text.lower() == "жабы")))
async def bio(message: types.Message):
    await message.answer("О ком хочешь узнать?", reply_markup=await get_friends_keyboard())


@user_private_router.callback_query(F.data.in_(FRIEND_INFO))
async def friend_info_callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.data
    user_data = FRIEND_INFO.get(user_id)
    if user_data:
        await callback.message.answer_photo(
            photo=user_data["photo"],
            caption=f"{html.bold(user_data['name'])}\n{user_data['bio']}",
            parse_mode=ParseMode.HTML,)


@user_private_router.callback_query(F.data == CALLBACK_BACK_TO_MAIN)
async def back_to_menu_callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "Выберите команду из меню",
        reply_markup=None
    )