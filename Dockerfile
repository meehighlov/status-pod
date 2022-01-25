FROM alpine:latest

RUN apk add --no-cache --update python3 py3-pip bash && add poetry

COPY . /webapp
WORKDIR /webapp
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry  \
    && poetry config virtualenvs.create false  \
    && poetry install --no-dev

RUN adduser -D statuspod
USER statuspod

EXPOSE 5000

ENTRYPOINT ["bash", "entrypoint.sh"]
