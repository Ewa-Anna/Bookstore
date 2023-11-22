FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . .
# COPY ./stripe/stripe_1.18.0_windows_x86_64/stripe /stripe/stripe

ENV CELERY_BROKER_URL=pyamqp://guest:guest@rabbitmq:5672//

CMD ["celery", "-A", "bookstore.celery", "worker", "-l", "info", "-P", "gevent"]