from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot:Bot):
    commands = [
        BotCommand(
            command='start',
            description='Start work'
        ),
        BotCommand(
            command='help',
            description='Help'
        ),
        BotCommand(
            command='cancel',
            description='Deny'
        ),
        BotCommand(
            command="info",
            description="Get an info about you"
        ),
        BotCommand(
            command="inline",
            description="Get inline buttons"
        )

    ]
    
    await bot.set_my_commands(commands, BotCommandScopeDefault())
    
