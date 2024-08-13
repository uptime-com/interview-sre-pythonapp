#!/bin/bash
set -eux -o pipefail

python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000
