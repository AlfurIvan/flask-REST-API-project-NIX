FROM python:3.8-slim-buster

WORKDIR /film_library

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]