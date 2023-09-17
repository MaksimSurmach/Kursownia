# Local Development Environment

## Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation)

## Setup

Clone the repository and install the dependencies:

```bash
poetry install
```
Or just use pip if you don't want to use poetry:
```bash
pip install -r requirements.txt
```


# Create env file

Create `.env` file in the root directory of the project and fill it with the following content:

```bash
# .env
TOKEN=your_secret_key
```
Fill `TOKEN` with your secret key of telegram bot.

## Running the server

```bash
poetry run Kursownia/main.py
```