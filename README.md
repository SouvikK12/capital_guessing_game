# capital_guessing_game

## Backend Setup

The first thing to do is to clone the repository

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ venv\Scripts\activate #for windows
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py makemigrations

(venv)$ python manage.py migrate

(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/v1/countries_and_capitals/`.


## Frontend Setup

The first thing to do is to clone the repository

install all dependencies:

```sh
$ npm install
```

start development server:

```sh
$ npm start
```
