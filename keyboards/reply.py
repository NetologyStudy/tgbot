from aiogram.types import  KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# start_kb = ReplyKeyboardMarkup(
#     keyboard= [
#         [
#             KeyboardButton(text="Мое расписание на месяц"),
#             KeyboardButton(text="Наши планы на месяц"),
#         ],
#         [
#             KeyboardButton(text="Жабы"),
#             KeyboardButton(text="Основные команды"),
#         ]
#     ],
#     resize_keyboard=True,
#     input_field_placeholder="Что вас интересует?"
# )


start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text="Мое расписание на месяц"),
    KeyboardButton(text="Наши планы на месяц"),
    KeyboardButton(text="Жабы"),
    KeyboardButton(text="Основные команды"),
)

start_kb.adjust(2)

del_kb = ReplyKeyboardRemove()