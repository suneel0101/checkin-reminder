# Objective
Create a system that sends you an SMS on same pre-set frequency. It asks you a question. You respond and that response is saved accordingly

# Requirements
## Prerequisites
- Python
- `pip`
- `virtualenv`
- [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/)
- Postgres 

# Dev Setup
1. Create a git repository / clone this one
2. `mkvirtualenv checkin`
3. `pip install -r requirements.txt`
4. `createdb checkin_db`
5. `python manage.py migrate`
6. `python manage.py runserver`


# Deployment
`git push heroku master`

# Recommended Tools
- Postico for a GUI for your postgres DBs