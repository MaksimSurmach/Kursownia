import os
import Kursownia
from Kursownia.commands import update_bot_commands, bot_default_commands, main_parser
from Kursownia.rates.local_storage import Storage
import telebot
import asyncio
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import logging

# Create logger
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)  # Outputs debug messages to console.
load_dotenv()

# Get the token from the environment variable
TOKEN = os.getenv('TOKEN')

# Create the bot object
bot = AsyncTeleBot(TOKEN, parse_mode=None)

# Create the storage object
storage = Storage()


async def scheduler():
    while True:
        # Update rates every 6 hours
        await storage.update_rates()
        await asyncio.sleep(60 * 60 * 6)


async def main():
    # Update bot commands in telegram
    await update_bot_commands(bot)

    # Default commands like start and help
    await bot_default_commands(bot)

    # Main text parser
    await main_parser(bot, storage)

    # Infinite loop to keep the bot running even when idle
    await asyncio.gather(bot.infinity_polling(), scheduler())


if __name__ == '__main__':
    # Run the main function as an async function in an asyncio loop
    print(f"Kursownia versions: {Kursownia.__version__()}")
    asyncio.run(main())
