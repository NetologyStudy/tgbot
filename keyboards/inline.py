from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from user_info import FRIEND_INFO


CALLBACK_BACK_TO_MAIN = "back_to_main_menu"


async def get_friends_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    for user_id, user_data in FRIEND_INFO.items():
        keyboard_builder.add(InlineKeyboardButton(
            text=user_data['name'],
            callback_data=user_id,
        )
    )
    keyboard_builder.row(InlineKeyboardButton(
        text="Назад",
        callback_data=CALLBACK_BACK_TO_MAIN
        )
    )
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


async def main_menu_kb():
    menu_kb = InlineKeyboardBuilder()
    menu_kb.add(InlineKeyboardButton(text="Жабы", callback_data=CALLBACK_BACK_TO_MAIN))
    return menu_kb.as_markup()
# async def back():
#     kb_back = InlineKeyboardBuilder()
#     kb_back.add(InlineKeyboardButton(
#         text="Назад",
#         callback_data=CALLBACK_BACK_TO_MAIN
#         )
#     )
#     return kb_back.as_markup()