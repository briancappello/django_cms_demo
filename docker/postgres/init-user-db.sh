#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER django_cms WITH PASSWORD 'django_cms';
    CREATE DATABASE django_cms;
    GRANT ALL PRIVILEGES ON DATABASE django_cms TO django_cms;
EOSQL
