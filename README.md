# Flask Application

## Initialize

1. Ensure postgres is installed on your system. see [here](https://www.postgresql.org/download/ "postgres install guildes")

2. use venv to isolate your code. create virtual environment with `python3 -m venv venv` and use virtual environment with `source venv/bin/activate`

3. install requirements with `pip install -r requirements.txt`

4. upgrade postgres database to latest with `alembic upgrade head`. This command will need to be run anytime there are changes to the database schema

## Execute

1. Ensure virtual environment is active, if not run `source venv/bin/activate`

2. Ensure pip packages are up to date. run `pip install -r requirements.txt`

3. run `python main.py`

## Unit Testing

1. Ensure postgres is installed and running

2. run `python -m pytest tests/`

3. ensure all unit tests pass. Fix any unit tests or code that was broken by you.