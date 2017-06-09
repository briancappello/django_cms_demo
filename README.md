# Django CMS Demo App

## Development

To start the development server:
```bash
$ sudo docker-compose build
$ sudo docker-compose up
```
And browse to http://localhost:8000

Login with user `admin` and password `pw`.

To open a terminal in the development environment:
```bash
$ sudo docker ps  # grab the container id/name from the list of running containers
$ sudo docker exec -it <container_ID_or_name> /bin/sh
```

To connect to the database:
```bash
$ psql -h localhost -p 5433 -U django_cms django_cms
```
