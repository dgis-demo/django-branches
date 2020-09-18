#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3 ./backend/manage.py makemigrations
python3 ./backend/manage.py migrate
python3 ./backend/manage.py loaddata ./backend/fixtures/fixtures.json

exec "$@"