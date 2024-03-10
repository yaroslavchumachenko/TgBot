from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, KeyboardButtonPollType

reply_keybord = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="1 Row, Button 1"
        ),
        KeyboardButton(
            text="1 Row, Button 2"
        ),
        KeyboardButton(
            text="Row 1, Button 3"
        )
    ],
    [
        KeyboardButton(
            text="2 Row, Button 1"
        )
    ],
    [
        KeyboardButton(
            text="3 Row, Button 1"
        ),
        KeyboardButton(
            text="3 Row, Button 2"
        )
    ]


], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Choose button 1", )

loc_tel_pol_keybord = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Request location",
            request_location= True
        ),
        KeyboardButton(
            text="Request telephone",
            request_contact=True
        ),
        KeyboardButton(
            text="Request poll",
            request_poll=KeyboardButtonPollType(type='regular')
        )
        
    ]
], one_time_keyboard=True)