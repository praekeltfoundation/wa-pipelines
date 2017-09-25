#!/bin/bash

set -ex

pip install -U -e '.[dev]' \
    && export DJANGO_SETTINGS_MODULE=wapipelines.tests.test_settings \
    && npm install bower \
    && django-admin makemigrations wapipelines \
    && django-admin migrate \
    && django-admin bower install \
    && django-admin collectstatic \
    && django-admin runserver
