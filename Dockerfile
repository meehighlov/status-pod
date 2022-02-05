FROM alpine:latest

RUN apk add --no-cache --update python3 py3-pip bash curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
RUN ~/.poetry/bin/poetry config virtualenvs.create false && ~/.poetry/bin/poetry install --no-dev

COPY . /app
WORKDIR /app

RUN adduser -D statuspod
USER statuspod

CMD python3 main.py bot
