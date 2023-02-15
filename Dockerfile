# ---
FROM python:3.10-alpine3.17 as base
# to use debian instead of alpine:
# FROM python:3.10-slim-bullseye as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/install/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.3.2 \
    VENV_PATH="/install/setup/.venv" \
    SETUP_PATH="/install/setup"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN mkdir /install

# ---
FROM base as builder

RUN apk add curl
# otherwise for debian:
# RUN apt-get update && apt-get install -y --no-install-recommends curl

RUN curl -sSL https://install.python-poetry.org | python -

WORKDIR $SETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-root --without dev,test

# ---
FROM base as production

ENV FASTAPI_ENV=production

COPY --from=builder $POETRY_HOME $POETRY_HOME
COPY --from=builder $SETUP_PATH/ $SETUP_PATH

COPY ./docker/entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY . /app
WORKDIR /app

ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8080"]
