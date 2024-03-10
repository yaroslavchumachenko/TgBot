from aiogram import Bot
from aiogram.types import CallbackQuery

async def sellect_macbook(call: CallbackQuery, bot:Bot):
    model = call.data.split("_")[1]
    size = call.data.split("_")[2]
    answer = f'{call.message.from_user.first_name}, you choose Apple Macbook {model} with number {size}'

    await call.message.answer(answer),
    await call.answer()