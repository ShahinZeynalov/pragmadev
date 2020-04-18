#!/bin/sh -ex
celery -A pdproject worker --loglevel=info &
celery -A pdproject beat --pidfile= -l info -S django &
tail -f /dev/nulls
