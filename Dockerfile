FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN curl -sSL https://cli.stripe.com/install | sh

COPY . .

# ENV CELERY_BROKER_URL=pyamqp://guest:guest@rabbitmq:5672//
# ENV INVENIO_CELERY_BROKER_URL = "amqp://guest:guest@mq:5672//"
