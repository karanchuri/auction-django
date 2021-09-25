FROM python:3

ENV PYTHONUNBUFFERED 1
ENV FLAVOUR=dev

RUN mkdir /src;
WORKDIR /src

COPY . /src
RUN pip3 install -r requirements.txt
RUN python3 manage.py collectstatic --noinput
EXPOSE 9000