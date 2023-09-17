from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_keyboard(currency_list: list, amount: float):
    max_col = 6
    max_row = 3
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = max_col
    for i in range(max_row):
        row = []
        for j in range(max_col):
            try:
                currency = currency_list[i * max_col + j]
                row.append(InlineKeyboardButton(currency, callback_data=f"{currency} {amount}"))
            except IndexError:
                break
        keyboard.add(*row)
    return keyboard

