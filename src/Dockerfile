FROM python:3.11.5-bullseye

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev

COPY . .
ENV PYTHONPATH="${PYTHONPATH}:/app"
CMD ["python", "Kursownia/main.py"]