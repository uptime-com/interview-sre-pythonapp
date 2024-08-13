# interview-sre-pythonapp
A sample python WSGI application prepared for deployment with Docker.

## Running
To run the app locally with docker compose, do the following:

    docker compose build
    docker compose up

Then browse to <http://localhost:8000> to view the application.

If you can see a shopping list, it's working!

## Cleaning Up
To stop & remove all containers, and clear all volumes (including the local database):

    docker compose rm -sfv
    docker compose down

## Database Access
The app runs with a PostgreSQL database. When running locally the database
is created as part of the compose stack.

The app's database access is controlled by four environment variables which
can be modified to control where the app connects:

    DATABASE_HOST=<hostname>
    DATABASE_USER=<username>
    DATABASE_PASS=<password>
    DATABASE_NAME=<database>
