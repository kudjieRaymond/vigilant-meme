FROM python:3.8-slim-buster

#Create the group and the user (with a home directory home/flash and a shell )  to be used in the container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask 

# Create the working directory and set is a the working directory
RUN mkdir -p /home/flask/app/web
WORKDIR /home/flask/app/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R flask:flaskgroup  /home/flask

USER flask