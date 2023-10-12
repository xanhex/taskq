FROM python:3.11.2-slim-buster

WORKDIR /app

COPY . .

RUN pip install --upgrade pip &&\
    pip install -r requirements_dashboard.txt --no-cache-dir
