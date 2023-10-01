import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot import formatting

from Kursownia.currency.parser import TextToCurrencyParser
from Kursownia.responses import generate_keyboard, message_template
from Kursownia.rates.local_storage import Storage
import Kursownia

async def update_bot_commands(bot: AsyncTeleBot):
    # remove old commands from telegram server
    await bot.delete_my_commands(scope=None, language_code=None)

    # set new commands
    await bot.set_my_commands(
        commands=[
            telebot.types.BotCommand("/start", "Start the bot"),
            telebot.types.BotCommand("/help", "Get help"),
        ],
    )


async def bot_default_commands(bot: AsyncTeleBot):
    """
    Default commands like start and help
    """

    @bot.message_handler(commands=['start'])
    async def send_welcome(message):
        # answer with markdown and formatting
        await bot.reply_to(message,
                           formatting.format_text(formatting.mbold(f'Hello, {message.from_user.first_name}!\n'),
                                                  formatting.mitalic('Welcome to the Currency Converter Bot! \n'),
                                                  formatting.mitalic(
                                                      'This handy bot is your go-to tool for quick currency '
                                                      'conversion. It uses the latest'
                                                      'exchange rates to help you convert currencies and perform '
                                                      'currency calculations effortlessly. \n'),
                                                  formatting.mitalic(
                                                  'To convert currency, type amount and currency name, for example:'),
                                                  formatting.mcode('100 usd \n'),
                                                  formatting.mbold('Key Features: \n'),
                                                  formatting.mbold('Real-Time Exchange Rates:'), formatting.mitalic(
                               'The bot uses up-to-date exchange rates to provide accurate currency conversions. \n'),
                                                  formatting.mbold('Easy to Use:'), formatting.mitalic(
                                   'Simply send the amount and currency you want to convert, and the bot will do the '
                                   'rest. \n'),
                                                  formatting.mbold('No Data Storage:'), formatting.mitalic(
                                   'Your financial data is not stored, ensuring your privacy and security. \n'),
                                                  formatting.mbold('Multiple Currency Support:'), formatting.mitalic(
                               'Convert between various currencies, including USD, EUR, PLN, and BYN, with ease. \n'),
                                                  formatting.mitalic(
                                                      'Enjoy hassle-free currency conversions with our Currency '
                                                      'Converter Bot! \n')),
                           parse_mode='MarkdownV2')

    @bot.message_handler(commands=['help'])
    async def send_help(message):
        await bot.reply_to(message, formatting.format_text(
            formatting.mbold("Version: " + Kursownia.__version__() + "\n"),
            formatting.mbold("How to use the bot:\n"),
            "type amount and currency name, for example:\n",
            formatting.munderline("100 usd\n"),
            "or type amount and then choose currency from the list",
            separator=" "
        ),
                           parse_mode='MarkdownV2')


async def main_parser(bot: AsyncTeleBot, storage: Storage):
    @bot.callback_query_handler(func=lambda call: True)
    async def callback_query(call):
        """
        Callback on currency button
        """
        # get currency and amount from callback data by splitting text
        currency, amount = call.data.split()
        # await bot.answer_callback_query(call.id, f"{amount} {currency}") # debug
        msg = message_template(float(amount), currency, storage)
        # prepare message and send it
        await bot.answer_callback_query(call.id, f"Converted {amount} {currency}")
        await bot.send_message(call.message.chat.id, msg, parse_mode='MarkdownV2')

    @bot.message_handler(content_types=['text'])
    async def parse_text_to_currency(message):
        """
        Main text parser, he tries to find currency and amount in message
        """
        # parse message
        result = TextToCurrencyParser(message.text.lower())

        # check if currency and amount found
        if result.currency and result.amount:
            text = message_template(result.amount, result.currency, storage)
            await bot.reply_to(message, text, parse_mode='MarkdownV2')

        # check if currency not found but have amount
        elif not result.currency and result.amount:
            # reply keyboard with all currencies
            keyboard = generate_keyboard(storage.currencies, result.amount)
            await bot.reply_to(message, 'Choose currency:', reply_markup=keyboard)

        # if cant find anything
        else:
            # no currency found
            await bot.reply_to(message, f'No currency found in your message. Please try again.')
