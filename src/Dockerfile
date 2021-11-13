# syntax=docker/dockerfile:1
FROM python:3.8-alpine

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY redis_exporter.py /usr/local/bin/redis_exporter.py

CMD [ "python3", "/usr/local/bin/redis_exporter.py" ]
