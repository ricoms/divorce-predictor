FROM python:3.8-buster AS BASE

LABEL maintainer="ricardosavi@g.com"

ENV PATH=/usr/local/bin:$PATH \
    PYTHONUNBUFFERED=TRUE \
    PYTHONDONTWRITEBYTECODE=TRUE \
    WORKSPACE_TMP="/opt/reports" \
    POETRY_VERSION=1.1.4

# hadolint ignore=DL3008
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION" \
    && mkdir -p /opt/program \
    && mkdir -p /opt/reports

WORKDIR /opt/program
COPY . /opt/program

ARG ENVIRON="production"

# hadolint ignore=SC2046
RUN poetry config virtualenvs.create false \
    && poetry install \
        $(if [ "$ENVIRON" = 'production' ]; then echo '--no-dev'; fi) \
        --no-interaction --no-ansi
