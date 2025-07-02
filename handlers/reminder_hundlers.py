from aiogram import  Router, F
from aiogram.types import Message
from aiogram.filters import  Command
from aiogram.fsm.context import FSMContext

from handlers.state import Reg

reminder_router = Router()


@reminder_router.message(Command("reg"))
async def reg_cmd(message: Message, state: FSMContext):
    await message.answer("Введите свое имя")
    await state.set_state(Reg.name)

@reminder_router.message(Reg.name)
async def cmd_reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отправьте ваше фото")
    await state.set_state(Reg.photo)

@reminder_router.message(Reg.photo, F.photo)
async def reg_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer_photo(data["photo"], caption=f"Имя: {data['name']}. Вы успешно прошли регистрацию!")
    await state.clear()