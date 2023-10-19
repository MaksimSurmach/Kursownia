# Kursownia
Telegram bot for currency exchange rate checks.

Kursownia allows you to message a bot within Telegram to get information on currency exchange rates.

Gets rates from:
1. [NBP API](https://api.nbp.pl/)
2. [NBRB API]()
3. [AlfaBank API]()

# Libraries
Kursownia uses a few libraries/apis to create a bot and connect to Telegram.
1. See [Telegram Bot Api](https://core.telegram.org/bots/api)
2. See [PyTelegram Bot Api](https://pytba.readthedocs.io/en/latest/index.html)

# Installation
Uses [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency installation.
1. After cloning the repository, use 
```bash
poetry install
```
2. Create a bot token through [Telegram](https://core.telegram.org/bots/features#botfather)
   1. In telegram, run `/newbot`
   2. Follow the on screen instructions to generate a token.
3. Create a `.env` file in the root of the project.
4. In the `.env` file, paste 
```bash
TOKEN=token_from_step2
```
5. To run the server, run
```bash
poetry run Kursownia/main.py
```