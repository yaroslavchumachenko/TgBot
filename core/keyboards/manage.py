from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


# main = ReplyKeyboardMarkup(resize_keyboard=True)
# main.add("Catalog").add("Crate").add("Contacts")

# main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
# main_admin.add("Catalog").add("Crate").add("Contacts").add("Admin panel")

# admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
# admin_panel.add("Add").add("Delete").add("Spam")
main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Catalog"
        ),
        KeyboardButton(
            text="Crate"
        ),
        KeyboardButton(
            text="Contacts"
        )
    ]


], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Choose button 1", )

main_admin = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Catalog"
        ),
        KeyboardButton(
            text="Crate"
        ),
        KeyboardButton(
            text="Contacts"
        ),
        KeyboardButton(
            text="Admin"
        )
    ]

], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Choose button 1", )

admin_panel = ReplyKeyboardMarkup(keyboard=[
    
    [
        KeyboardButton(
            text="Add"
        ),
        KeyboardButton(
            text="Delete"
        ),
        KeyboardButton(
            text="Spam"
        )
    ]


], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Choose button 1", )




manage_item = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(
        text="T-shirts",
        url = ""
    ),
    InlineKeyboardButton(
        text="Shorts",
        callback_data = ""
    ),
    InlineKeyboardButton(
        text="Boots",
        url=""
    )
    ]

])  