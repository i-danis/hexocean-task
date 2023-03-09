FROM python:3.10-slim

WORKDIR /app

RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-root

COPY src src

CMD cd src

CMD poetry run python src/manage.py migrate
CMD poetry run python src/manage.py runserver 0.0.0.0:8000
