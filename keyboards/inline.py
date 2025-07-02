from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import FRIEND_INFO, schedule

CALLBACK_BACK_TO_MAIN = "back_to_main_menu"
CALLBACK_SHOW_FRIENDS = "show_friends"
CALLBACK_BACK_TO_FRIENDS = "back_to_friends"


def get_friends_keyboard():
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


def back_to_friends_kb():
    kb_back = InlineKeyboardBuilder()
    kb_back.add(InlineKeyboardButton(text="Назад", callback_data=CALLBACK_BACK_TO_FRIENDS))
    return kb_back.as_markup()


def main_menu_kb():
    menu_kb = InlineKeyboardBuilder()
    menu_kb.add(InlineKeyboardButton(text="Жабы", callback_data=CALLBACK_SHOW_FRIENDS))
    return menu_kb.as_markup()



def my_schedule_kb():
    schedule_kb = InlineKeyboardBuilder()
    for days, hours in schedule.items():
        schedule_kb.add(InlineKeyboardButton(text=f"{days}",
                                             callback_data=days
                                             )
                        )
    return schedule_kb.as_markup()
