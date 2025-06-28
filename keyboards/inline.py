from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from user_info import FRIEND_INFO

def get_friends_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    for user_id, user_data in FRIEND_INFO.items():
        keyboard_builder.add(InlineKeyboardButton(
            text=user_data['name'],
            callback_data=user_id,
        )
    )
    keyboard_builder.adjust(2)
    return keyboard_builder
