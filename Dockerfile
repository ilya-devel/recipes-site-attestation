FROM python:3.10.1-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /web_django/my_site
WORKDIR /web_django/my_site
COPY requirements.txt /web_django/
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y default-libmysqlclient-dev build-essential
RUN pip install --upgrade pip && pip install -r ../requirements.txt
ADD . /web_django/