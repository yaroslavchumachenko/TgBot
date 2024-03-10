from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
import asyncio
import logging
from core.handlers.basic import get_started, get_photo, get_hello, get_info
from core.handlers.contact import get_fake_contact, get_true_contact
# from core.filters.iscontact import IsTrueContact
from core.settings import settings
from aiogram.filters import ExceptionTypeFilter, Command
from core.utils.commands import set_commands
from core.handlers.basic import get_inline
from core.handlers.callback import sellect_macbook
from core.handlers.db_handler import on_startup
# from core.keyboards.manage import main, main_admin, admin_panel
from dotenv import load_dotenv
import os
load_dotenv()

async def start_bot(bot: Bot): 
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id,text = "Bot started!")
    # await message.answer(f"Wellcome to the shop!", reply_markup=main)
    # if message.from_user.id == int(os.getenv('ADMIN_ID')):
    #     await message.answer(f"You authorised as Admin!", reply_markup=main_admin)
    
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Bot stopped")



async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    
    bot = Bot(token = settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)


    dp.message.register(get_started, Command(commands=["start", "run"]))
    dp.message.register(get_photo, F.content_type == ContentType.PHOTO)
    dp.message.register(get_hello, F.text == "Hello")
    dp.message.register(get_info, Command(commands=["info"]))
    # dp.message.register(get_true_contact, F.content_type == ContentType.CONTACT and IsTrueContact())
    # dp.message.register(get_fake_contact, F.content_type == ContentType.CONTACT)
    dp.message.register(get_inline, Command(commands=["inline"]))
    dp.callback_query.register(sellect_macbook, F.data.startswith("apple_"))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
    asyncio.run(on_startup())