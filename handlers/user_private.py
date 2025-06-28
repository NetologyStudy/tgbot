from aiogram import types, Router, html, F
from aiogram.enums import ParseMode
from aiogram.filters import or_f
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery

from keyboards.inline import get_friends_keyboard
from keyboards.reply import start_kb, del_kb

from user_info import  FRIEND_DATA, FRIEND_INFO

user_private_router = Router()


TEXT = """
/start - запуск жабобота
/help - помощь для дурачков
/bio - жабы
"""


@user_private_router.message(Command("start"))
async def start_command(message: types.Message):
    user_name = message.from_user.username
    full_name = message.from_user.full_name
    sticker_id = FRIEND_DATA.get(user_name)
    await message.answer(
        f"Привет, {html.bold(full_name)}! 😎",
        parse_mode=ParseMode.HTML,
        reply_markup=start_kb.as_markup(
            resize_keyboard=True,
            input_field_placeholder="Что вас интересует?",
        )
    )
    if sticker_id:
        await message.answer_sticker(sticker_id)
    else:
        await message.answer(f"Привет, {html.bold(full_name)}! 😎", parse_mode=ParseMode.HTML)


@user_private_router.message(or_f(Command("help"), (F.text.lower() == "основные команды")))
async def help_command(message: types.Message):
    await message.answer(TEXT, reply_markup=del_kb)


@user_private_router.message(or_f(Command("bio"), (F.text.lower() == "жабы")))
async def bio(message: types.Message):
    await message.answer("О ком хочешь узнать?", reply_markup=get_friends_keyboard().as_markup())


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