FROM python:3.11.5-bullseye

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry install

CMD ["poetry", "run", "python", "-m", "Kursownia.main"]
