#!/usr/bin/env bash
python /code/bookstore/manage.py migrate
python /code/bookstore/manage.py runserver 0.0.0.0:8000