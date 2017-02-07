FROM python:3.6-alpine
RUN apk add --update --no-cache \
    build-base \
    postgresql-dev

WORKDIR /app
RUN mkdir ./static

COPY ./ /app/
RUN pip3 install -r requirements.txt

WORKDIR /app/todoer

EXPOSE 8000

CMD exec gunicorn -w 4 -b :8000 todoer.wsgi
