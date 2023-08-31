# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /broadcastservice

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY api api/
COPY services services/
COPY templates templates/
COPY *.py ./

CMD ["python3", "main.py"]
