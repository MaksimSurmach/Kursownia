import asyncio
import os
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

keywords = {
    'USD': ['dollar', 'usd', 'dolar', 'dolara', 'dolary', 'dolarow', '$', 'баксов', 'бакс', 'долларов', 'доллар', 'доллара'],
    'EUR': ['euro', 'eur', 'euro', 'euro', 'euro', 'euro', '€', 'евро', 'евро', 'евро', 'евро', 'евро'],
    'PLN': ['zloty', 'pln', 'zloty', 'zlotego', 'zlotych', 'zlotow', 'zł', 'злотых', 'злотых', 'злотых', 'злотых', 'злотых'],
    'RUB': ['rubl', 'rub', 'rubl', 'rublya', 'rubley', 'rubley', '₽', 'рублей', 'рублей', 'рублей', 'рублей', 'рублей'],
    'UAH': ['grivna', 'uah', 'grivna', 'grivny', 'griven', 'griven', '₴', 'гривен', 'гривен', 'гривен', 'гривен', 'гривен'],
    'BYN': ['rubl', 'rub', 'rubl', 'rublya', 'rubley', 'rubley', '₽', 'рублей', 'рублей', 'рублей', 'рублей', 'рублей', 'белорусски']
}

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.reply_to(message, f'Hello, {message.from_user.first_name}!' +
    '\n' + 'I am a bot that shows current exchange rates.' +
    '\n' + 'To see the current euro rate, type /euro' )


@bot.message_handler(commands=storage.currencies, ignore_case=True)
async def send_dollar_rate(message):
    currency = message.text[1:]
    logger.info(f'User {message.from_user.first_name} requested {currency} rate')
    data = storage.get_currency(currency).get_all_rates()
    text = f'Current {currency} rate is'
    for curr in data:
        if curr == currency:
            continue
        text += f'\n{curr}: {data[curr]["sell"]}'
    await bot.reply_to(message, text)

@bot.message_handler(ignore_case=True)
async def parse_text_to_currency(message):
    logger.info(f'Requested {message.text}')
    text = message.text.lower()
    #remove all numbers from text
    text = text.translate(str.maketrans('', '', string.digits))
    for currency in keywords:
        for keyword in keywords[currency]:
            if keyword in text:
                logger.info(f'User {message.from_user.first_name} requested {currency} rate')
                await bot.reply_to(message, f'Resolve as {currency}')



async def scheduler():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(bot.infinity_polling(), scheduler())



if __name__ == '__main__':
    asyncio.run(main())