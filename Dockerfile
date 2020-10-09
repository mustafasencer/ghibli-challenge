FROM python:3.7

MAINTAINER Mustafa Sencer Özcan "m.sencerozcan@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip -r /requirements.txt

ADD . /ghibli-challenge

WORKDIR /ghibli-challenge

COPY . /ghibli-challenge

CMD python app.py