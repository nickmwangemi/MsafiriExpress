# Msafiri-Express

This is a bus ticketing application.

On the frontend, users can view multiple destinations which they can then book tickets to.

On the backend, admin users are presented with an admin area to manage various site resources including destinations, tickets, prices and contact inquiries made by customers.


## Local Setup
Before setting up, please make sure that you have Python3.6+ installed and running on your machine.

1.  Clone the repo
```bash
  git clone git@github.com:nickmwangemi/MsafiriExpress.git
```

2. Change directory into the project folder
```bash
  cd MsafiriExpress
```

3. Setup virtual environment and activate it
```bash
  virtualenv env
  source env/bin/activate
```

4. Install dependencies
```bash
  pip3 install -r requirements.txt
```

5. Ensure you have PostgreSQL installed and running. Create a postgresql user with username and password msafiri, and create a corresponding database called msafiri.
```bash
  sudo su - postgres -c 'createuser -d -P msafiri'
  sudo su - postgres -c 'createdb msafiri'
```

6. You also have the option of exporting a custom database connection string as an environment variable named DATABASE_URL which will take precedence over the default.
```bash
  export DATABASE_URL=postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE_NAME>
```

7. Run migrations to create database tables.
```bash
  python manage.py migrate
```

8. Create a superuser account
```bash
  python manage.py createsuperuser
```

7. Run server
```bash
  python manage.py runserver
```

The server should be available at [http://127.0.0.1:8000](http://127.0.0.1:8000), while the admin panel will be at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


## Setup pre-commit
The project has linting enabled using pre-commit. It runs on the CI pipeline, so you need to enable locally as well. Run the following to allow Precommit to format and fix any linting errors on your code.
```
pre-commit install
```

## Tech Stack
This application is built using HTML, CSS and Bootstrap on the frontend, Django on the backend and Postgresql for the database.


## Live Demo
A live demo of this project is available at: [Msafiri Express](https://msafiriexpress.herokuapp.com/)
