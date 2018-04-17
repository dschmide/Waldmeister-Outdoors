# Waldmeister-Outdoors

"Waldmeister-Outdoors" ist eine Applikation, welche es ermöglicht, 
Waldstandorte in der Schweiz zu erforschen und zu erfassen.

## TODO - next steps

The most likely next steps to advance towards completion of the application:

### Frontend

* Use something like `https://www.npmjs.com/package/vuejs-jwt`
  or follow the guide at `https://hackernoon.com/jwt-authentication-in-vue-js-and-django-rest-framework-part-1-c40c5c0d4f6e`
* Make the interface work
* Usability (when can what be pressed? What is possible as anonymous User?)
* Get everything working that is on the page
* move from static geojson to API

### Backend

* Remove templates and use API calls for frontend interaction
* Clean up the code and add the required functionality to interact
  with the frontend

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
