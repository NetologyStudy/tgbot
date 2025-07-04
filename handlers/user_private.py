import asyncio

from aiogram import Router, html, F
from aiogram.enums import ParseMode
from aiogram.filters import or_f
from aiogram.filters.command import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ChatAction

from keyboards.inline import get_friends_keyboard, CALLBACK_BACK_TO_MAIN, main_menu_kb, my_schedule_kb, \
    CALLBACK_SHOW_FRIENDS, back_to_friends_kb, CALLBACK_BACK_TO_FRIENDS

from data import FRIEND_DATA, FRIEND_INFO, schedule

user_private_router = Router()


TEXT = """
/start - запуск жабобота
/help - помощь для дурачков
/bio - жабы
"""



@user_private_router.message(Command("schedule"))
async def my_schedule(message: Message):
    await message.answer("Выберите день", reply_markup=await my_schedule_kb())




@user_private_router.message(CommandStart())
async def start_command(message: Message):
    user_name = message.from_user.username
    full_name = message.from_user.full_name
    sticker_id = FRIEND_DATA.get(user_name)
    await message.bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING,
    )
    await asyncio.sleep(1.5)
    await message.answer(
        f"""Привет, {html.bold(full_name)}! Я помогу тебе использовать свободное время с пользой!
Зарегистрируйтесь, чтобы продолжить:  /reg""",
        parse_mode=ParseMode.HTML,
    )

    if sticker_id:
        await message.bot.send_chat_action(
            chat_id=message.from_user.id,
            action=ChatAction.CHOOSE_STICKER,
        )
        await asyncio.sleep(1)
        await message.answer_sticker(sticker_id)



@user_private_router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        f"""Что я умею:

    /bio - Информация о наших жабах
            """
    )


@user_private_router.message(Command("menu"))
async def show_main_menu(message: Message):
    await message.answer("Главное меню", reply_markup=main_menu_kb())


@user_private_router.message(or_f(Command("bio"), (F.text.lower() == "жабы")))
async def bio(message: Message):
    await message.bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING,
    )
    await asyncio.sleep(1.5)
    await message.answer("О ком хочешь узнать?", reply_markup=get_friends_keyboard())


@user_private_router.callback_query(F.data == CALLBACK_SHOW_FRIENDS)
async def friend_info_callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("О ком хочешь узнать?", reply_markup=get_friends_keyboard())


@user_private_router.callback_query(F.data.in_(FRIEND_INFO))
async def show_friend_info_callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    user_id = callback.data
    user_data = FRIEND_INFO.get(user_id)
    if user_data:
        await callback.message.answer_photo(
            photo=user_data["photo"],
            caption=f"{html.bold(user_data['name'])}\n{user_data['bio']}",
            parse_mode=ParseMode.HTML,
            reply_markup=back_to_friends_kb())


@user_private_router.callback_query(F.data == CALLBACK_BACK_TO_FRIENDS)
async def back_to_friends_callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer("О ком хочешь узнать?", reply_markup=get_friends_keyboard())


@user_private_router.callback_query(F.data == CALLBACK_BACK_TO_MAIN)
async def back_to_menu_callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "Главное меню",
        reply_markup=main_menu_kb()
    )


@user_private_router.callback_query(F.data.in_(schedule))
async def my_schedule_callback_query_handler(callback: CallbackQuery):
    await callback.answer()
