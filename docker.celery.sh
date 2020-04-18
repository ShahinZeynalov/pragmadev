#!/bin/sh -ex
celery -A pdproject worker --loglevel=info
