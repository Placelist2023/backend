#!/bin/bash

echo "Running python manage.py $* inside of the web_svc container"
docker-compose run --rm web_svc sh -c "python manage.py $*"
