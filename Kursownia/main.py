import asyncio
import telebot
import aioschedule
from telebot.async_telebot import AsyncTeleBot
import logging
from rates.rate_getter import request_euro_rate, request_dollar_rate

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)  # Outputs debug messages to console.

bot = AsyncTeleBot("6693432806:AAGu7LPbIn-Ge98CARF17SvR3m3VGE-hDsQ", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await message.reply("Hello, I'm Kursownia!")


@bot.message_handler(commands=['euro'])
async def send_euro_rate(message):
    await bot.reply_to(message, f'Current euro rate: {request_euro_rate()}')


@bot.message_handler(commands=['dollar'])
async def send_dollar_rate(message):
    await bot.reply_to(message, f'Current dollar rate: {request_dollar_rate()}')



async def scheduler():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(bot.infinity_polling(), scheduler())


if __name__ == '__main__':
    asyncio.run(main())