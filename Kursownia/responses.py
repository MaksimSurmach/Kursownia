from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import formatting

EMOJI = {
    "USD": "🇺🇸",
    "EUR": "🇪🇺",
    "PLN": "🇵🇱",
    "BYN": "🇧🇾",
}

def generate_keyboard(currency_list: list, amount: float):
    """
    Generate keyboard with all currencies
    """
    max_col = 6  # max columns in keyboard
    max_row = 3  # max rows in keyboard
    keyboard = InlineKeyboardMarkup()  # keyboard object
    keyboard.row_width = max_col  # set max columns
    # Create buttons matrix
    for i in range(max_row):
        row = []
        for j in range(max_col):
            try:
                currency = currency_list[i * max_col + j]
                row.append(InlineKeyboardButton(currency, callback_data=f"{currency} {amount}"))
            except IndexError:
                # if no more currencies, break
                break
        # add row to keyboard
        keyboard.add(*row)
    return keyboard


def message_template(amount: float, currency: str, storage):
    """
    Generate message with all currencies
    """
    text_body = ''
    for curr in storage.currencies:
        if curr == currency:
            continue
        text_body += f'{EMOJI[curr]}  {storage.calculate(currency, curr, amount)}\n'
    return formatting.format_text(
        formatting.mbold(text_body),
        separator='\n'
    )
