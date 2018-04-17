# Waldmeister-Outdoors

"Waldmeister-Outdoors" ist eine Applikation, welche es ermöglicht, 
Waldstandorte in der Schweiz zu erforschen und zu erfassen.

## Installation

Clone Repository

install dependencies (VueServer in `client` folder)

npm install

install python dependencies (`backend` folder)

pip install -r requirements.txt

start dev server (root folder) 

python3 manage.py runserver

start Vue-Server (client folder) 

npm start

Once the Servers are running, you can visit the site using the URL displayed on the Vue-Server window

Migrate database 

python3 manage.py migrate

For this Project, a PostgreSQL is used by Django. Either create a database called "dschwaldmeister" with port 5435 and username Postgres, or change the values in the settings.py file within the Django directory.
