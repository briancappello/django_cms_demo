FROM alpine:3.5

ENV PYTHONUNBUFFERED 1

# install gcc and friends
RUN apk add --no-cache build-base

# install python3.5 and latest pip/setuptools
RUN apk add --no-cache python3 python3-dev && \
	python3 -m ensurepip && \
	rm -r /usr/lib/python*/ensurepip && \
	pip3 install --upgrade pip setuptools && \
	if [ ! -e /usr/bin/pip ]; then ln -s /usr/bin/pip3 /usr/bin/pip; fi && \
	if [ ! -e /usr/bin/python ]; then ln -s /usr/bin/python3 /usr/bin/python; fi

# requirements for installing psycopg2
RUN apk add --no-cache postgresql-dev

# FIXME git only required for installing pip deps from github
RUN apk add --no-cache git

# requirements for building Pillow
RUN apk add --no-cache jpeg-dev zlib-dev

# requirements for building lxml
RUN apk add --no-cache libxml2-dev libxslt-dev

COPY ./requirements.txt /django/
RUN pip install -r /django/requirements.txt

# cleanup pip cache
RUN rm -r /root/.cache

COPY ./docker/backend/run-django.sh /

WORKDIR /django
