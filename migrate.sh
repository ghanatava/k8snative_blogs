#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@admin.com"}


cd /app/

python manage.py migrate --noinput
(echo "from django.contrib.auth.models import User; User.objects.create_superuser($DJANGO_SUPERUSER_NAME,$SUPERUSER_EMAIL,$DJANGO_SUPERUSER_PASSWORD)" | python3 manage.py shell) || true