FROM python:3.8-slim-buster

WORKDIR /flask_film_lib

COPY requirements.txt requirements.txt
RUN apt-get update
RUN mkdir /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /app
COPY . /app
COPY . .

EXPOSE 5000

CMD ['gunicorn', '-w', '4','--bind', '0.0.0.0:5000', 'wsgi:application']
