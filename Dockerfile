FROM python:3.6-jessie

ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y sqlite3 libsqlite3-dev

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python3 counter/manage.py flush --no-input

EXPOSE 8000
