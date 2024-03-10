from aiogram.filters import BaseFilter
from aiogram.types import Message
import os


class IsTrueContact(BaseFilter):
    async def __call__(self, message:Message):
        if message.from_user.id == int(os.getenv('ADMIN_ID')):
            return True
        else:
            return False