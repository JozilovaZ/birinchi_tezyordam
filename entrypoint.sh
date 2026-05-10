#!/bin/sh
set -e

mkdir -p /app/data

echo ">>> Migratsiyalar bajarilmoqda..."
python manage.py migrate --noinput

echo ">>> Static fayllar yig'ilmoqda..."
python manage.py collectstatic --noinput

echo ">>> Boshlang'ich ma'lumotlar yuklanmoqda..."
python manage.py yuklash

echo ">>> Gunicorn ishga tushmoqda..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
