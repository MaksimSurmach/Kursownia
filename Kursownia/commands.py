import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot import formatting

async def update_bot_commands(bot: AsyncTeleBot):
    await bot.delete_my_commands(scope=None, language_code=None)

    await bot.set_my_commands(
        commands=[
            telebot.types.BotCommand("/start", "Start the bot"),
            telebot.types.BotCommand("/help", "Get help"),
        ],
    )

async def bot_default_commands(bot: AsyncTeleBot):
    @bot.message_handler(commands=['start'])
    async def send_welcome(message):
        await bot.reply_to(message,formatting.format_text( formatting.mbold(f'Hello, {message.from_user.first_name}!\n'),
                           formatting.mitalic('Welcome to the Currency Converter Bot! \n'),
                           formatting.mitalic('This handy bot is your go-to tool for quick currency conversion. It uses the latest exchange rates to help you convert currencies and perform currency calculations effortlessly. \n'),
                           formatting.mitalic('To convert currency, type amount and currency name, for example:'),
                           formatting.mcode('100 usd \n'),
                           formatting.mbold('Key Features: \n'),
                           formatting.mbold('Real-Time Exchange Rates:'), formatting.mitalic('The bot uses up-to-date exchange rates to provide accurate currency conversions. \n'),
                           formatting.mbold('Easy to Use:'), formatting.mitalic('Simply send the amount and currency you want to convert, and the bot will do the rest. \n'),
                           formatting.mbold('No Data Storage:'), formatting.mitalic('Your financial data is not stored, ensuring your privacy and security. \n'),
                           formatting.mbold('Multiple Currency Support:'), formatting.mitalic('Convert between various currencies, including USD, EUR, PLN, and BYN, with ease. \n'),
                            formatting.mitalic('Enjoy hassle-free currency conversions with our Currency Converter Bot! \n')),
                           parse_mode='MarkdownV2')

    @bot.message_handler(commands=['help'])
    async def send_help(message):
        await bot.reply_to(message, formatting.format_text(
            formatting.mbold("How to use the bot:\n"),
            "type amount and currency name, for example:\n",
            formatting.munderline("100 usd\n"),
            "or type amount and then choose currency from the list",
            formatting.mcode("in dev stage"),
            separator=" " # separator separates all strings
        ),
        parse_mode='MarkdownV2')

