from aiogram import Bot
from aiogram.types import Message


async def get_true_contact(message:Message, bot:Bot, phone:str):
    await message.answer(f"You send yours contact! Your number is: {phone} ")

async def get_fake_contact(message:Message, bot:Bot):
    await message.answer("You send not yours contact!")