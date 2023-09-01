# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /broadcastservice

RUN apt-get update
RUN apt-get install -y chromium
RUN apt-get install -y imagemagick

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY api api/
COPY services services/
COPY templates templates/
COPY *.py ./
COPY ".env*" ./

CMD ["python3", "main.py"]
