FROM python:3.9.16-slim-bullseye

WORKDIR /app

COPY . /app

RUN apt update -y && apt install ffmpeg -y && pip install --upgrade pip && pip install -r requirements.txt

CMD [ "python","subtitle/manage.py","runserver","0.0.0.0:8000" ]