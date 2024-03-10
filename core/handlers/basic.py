from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keybord, loc_tel_pol_keybord
from core.keyboards.inline import select_macbook
from core.keyboards.manage import main, main_admin, admin_panel
import os
from dotenv import load_dotenv

load_dotenv()


async def get_started(message = Message, bot = Bot):
    await message.answer(f"Wellcome to the shop!", reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f"You authorised as Admin!", reply_markup= main_admin)

async def get_photo(message = Message, bot=Bot):
    await message.answer(f"Perfect, you send me this pic!")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'core/user_pics/photo.jpg')

async def get_hello(message = Message, bot = Bot):
    await message.answer(f"Hello, {message.from_user.first_name}!")

async def get_info(message = Message, bot = Bot):
    await bot.send_message(message.from_user.id, f'Choose an info: ', reply_markup=loc_tel_pol_keybord)


async def get_inline(message = Message, bot = Bot):
    await message.answer(f"Hello, {message.from_user.first_name}. I'll show you inline buttons!",
                            reply_markup=select_macbook)
    
