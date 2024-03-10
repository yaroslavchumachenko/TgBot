from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(
        text="Macbook 13",
        callback_data = "apple_13_M1"
    ),
    InlineKeyboardButton(
        text="Macbook 12",
        callback_data = "apple_12_M2"
    ),
    InlineKeyboardButton(
        text="Site",
        url="google.com"
    )
    ]

])  