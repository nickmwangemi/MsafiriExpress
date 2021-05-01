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

5. Create database (Please be sure to updated the database settings in PropertyWatch/settings.py to a database of your choosing i.e sqlite3, MySQL, PostgreSQL)
```bash
  python manage.py migrate
```

6. Create admin account
```bash
  python manage.py createsuperuser
```

7. Run server
```bash
  python manage.py runserver
```

The server should be available at [http://127.0.0.1:8000](http://127.0.0.1:8000), while the admin panel will be at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


## Tech Stack
This application is built using HTML, CSS and Bootstrap on the frontend, Django on the backend and Postgresql for the database.


## Live Demo
A live demo of this project is available at: [Property Watch](https://msafiriexpress.herokuapp.com/)
