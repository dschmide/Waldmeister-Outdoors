# Waldmeister-Outdoors

"Waldmeister-Outdoors" ist eine Applikation, welche es ermöglicht, 
Waldstandorte in der Schweiz zu erforschen und zu erfassen.

## Usage (with docker and docker-compose)

After a `docker-compose up --build` visit `https://localhost:8443`.
Under `https://localhost:8443/api` the backend/api is running.

If you need to debug one of either backend or frontend, see
the `docker-compose.yml` file for the port that these applications
are running on.

### Prerequisites

* Docker and docker-compose setup on your local machine.


### Setup

Use `docker-compose build --pull` to build and update existing images. 

### Start

Use `docker-compose up` to start the applications. If you want to start
the services in the background, use `docker-compose up -d` and 
`docker-compose logs -f` to display the logs. For details on how to use 
docker-compose, refer to the compose documentation.

### Create a superuser

Run `docker-compose run --rm backend python manage.py createsuperuser`
to create a superuser for this instance.

### Database

The database is being started automatically when using docker-compose.

## Deploying

### Build and push new images

* `docker-compose -f docker-compose.push.yml build --pull`
* `docker-compose -f docker-compose.push.yml push`

### Deploy on server

Using your choice of server, deploy the service using
the images `waldmeister/map-frontend` for the frontend
and `waldmeister/map-api` for the backend.
