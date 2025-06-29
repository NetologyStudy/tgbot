from aiogram.types import  KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

async def back_to_menu():
    start_kb = ReplyKeyboardBuilder()
    start_kb.add(
        KeyboardButton(text="Главное меню"),
    )

    start_kb.adjust(2)
    return start_kb.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Вернутся в главное меню",
    )
