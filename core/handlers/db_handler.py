from aiogram import Bot
from aiogram.types import Message
from core.database import database
async def on_startup():
    await database.db_start()
    print("Bot started!")

