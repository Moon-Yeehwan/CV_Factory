#!/bin/bash
mkdir -p /app/logs
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000 