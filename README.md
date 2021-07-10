# CSE 3200: System Development Project

This project uses [python](https://www.python.org/) version 3.9.5 and [Django](https://www.djangoproject.com/) version 3.2.4

## Installing the Dependencies

* Run `pip install -r requirements.txt` to install the dependencies.

It is recommended to use a virtual environment.

## Applying the Migrations

Go to the project root directory
* Run `python manage.py makemigrations` to make migration files
* Run `python manage.py migrate` to apply the migrations to the database
* Run `python manage.py check` to check for any errors

## Run the Server

If no errors from migrations
* Run `python manage.py runserver` to run the server
* The server should open in `http://localhost:8000/`
* Use `Ctrl + C` or `Ctrl + pause/break` to shut down the server

## Accessing the Admin Panel

* Run `python manage.py createsuperuser` to create a superuser to log into the admin panel
* Give `username, email & password` of choice
* Go to `http://localhost:8000/admin/` to log into the admin panel

## Testing 

* Run `python manage.py test` to test the application

## Further Help

To get more help on Django Command line run `python manage.py help` or go check out the [django-admin and manage.py](https://docs.djangoproject.com/en/3.1/ref/django-admin/) page.
