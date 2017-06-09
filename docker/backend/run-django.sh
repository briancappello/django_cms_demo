#!/bin/sh

until python manage.py migrate
do
    echo "waiting for the database to become available..."
    sleep 2
done

python manage.py loaddata fixtures.json
python manage.py runserver 0.0.0.0:8000
