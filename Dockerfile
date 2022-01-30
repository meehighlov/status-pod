FROM alpine:latest

RUN apk add --no-cache --update python3 py3-pip bash

COPY . /webapp
WORKDIR /webapp
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN apk add curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
RUN ~/.poetry/bin/poetry config virtualenvs.create false && ~/.poetry/bin/poetry install --no-dev

RUN adduser -D statuspod
USER statuspod

CMD python3 main.py bot
