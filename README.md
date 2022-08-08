# OmbrébyART'i

Aarti's portfolio project.

## Installation

Create a new virtual environment and activate it.

```bash
$ python -m venv venv
$ source venv/bin/activate
```

Install the required libraries:

```bash
$ pip install -r requirements.txt -c constraints.txt
```

Create the database in PostgreSQL:

```bash
$ psql -U postgres
postgres=# CREATE DATABASE ombre_main;
```

Run the pending migrations:

```bash
$ python manage.py migrate
```
