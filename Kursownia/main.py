import asyncio
import os

from Kursownia.commands import update_bot_commands, bot_default_commands
from Kursownia.currency.parser import TextToCurrencyParser
from Kursownia.keyboards import generate_keyboard
from Kursownia.rates.local_storage import Storage
import telebot
import aioschedule
import asyncio
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import logging
import string

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)  # Outputs debug messages to console.
load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = AsyncTeleBot(TOKEN, parse_mode=None)

storage = Storage()

async def main_parser(bot: AsyncTeleBot):
    @bot.callback_query_handler(func=lambda call: True)
    async def callback_query(call):
        logger.info(f'Requested: {call.data}')
        currency, amount = call.data.split()
        await bot.answer_callback_query(call.id, f"{amount} {currency}")
        text = f'{amount} {currency} is'
        for curr in storage.currencies:
            if curr == currency:
                continue
            text += f'\n{storage.calculate(currency, curr, float(amount))} {curr}'
        await bot.send_message(call.message.chat.id, text)

    @bot.message_handler(content_types=['text'])
    async def parse_text_to_currency(message):
        logger.info(f'Requested: {message.text}')
        result = TextToCurrencyParser(message.text.lower())
        logger.info(f"Parse as currency: {result.currency}, as amount: {result.amount}")
        if result.currency and result.amount:
            text = f'{result.amount} {result.currency} is'
            for curr in storage.currencies:
                if curr == result.currency:
                    continue
                text += f'\n{storage.calculate(result.currency, curr, result.amount)} {curr}'
            await bot.reply_to(message, text)

        elif not result.currency and result.amount:
            #reply keyboard with all currencies
            keyboard = generate_keyboard(storage.currencies, result.amount)
            await bot.reply_to(message, 'Choose currency:', reply_markup=keyboard)

        else:
            await bot.reply_to(message, f'No currency found in your message. Please try again.')


# @aioschedule.every(1).minutes.do
# async def update_rates_schedule():
#     logger.info('Updating rates')
#     storage.update_rates()


async def scheduler():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main():
    await storage.update_rates()
    # aioschedule.every(1).minutes.do(storage.update_rates())
    await update_bot_commands(bot)
    await bot_default_commands(bot)
    await main_parser(bot)
    await asyncio.gather(bot.infinity_polling(), scheduler())


if __name__ == '__main__':
    asyncio.run(main())