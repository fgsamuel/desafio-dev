#!/usr/bin/env bash

set -e

python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
gunicorn cnab_reader.wsgi -b 0.0.0.0:8000
