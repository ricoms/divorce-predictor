FROM python:3.8-buster

ENV PATH=/usr/local/bin:$PATH \
    PYTHONUNBUFFERED=TRUE \
    PYTHONDONTWRITEBYTECODE=TRUE \
    WORKSPACE_TMP="/opt/reports" \
    POETRY_VERSION=1.1.11

# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir "poetry==$POETRY_VERSION" \
    && rm -r /var/lib/apt/lists/* \
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

EXPOSE 8080
ENTRYPOINT [ "uvicorn" ]
CMD ["divorce_predictor.api.api:app", "--host", "0.0.0.0", "--port", "8080"]
