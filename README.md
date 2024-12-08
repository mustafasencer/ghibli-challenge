# Studio Ghibli Movies

In this project, a simple `Flask` application is created to list the movies of Studio Ghibli.

## Installation

First and foremost `docker` and `docker-compose` should be installed on your local machine.

The following commands will run the `Flask` application on `http://localhost:8000`.

```console
docker-compose build
docker-compose up -d
```

## API Documentation

API provides movie listing logic along with the index page content.

- [Index](/app/api.md): `GET /`
- [Get Movies](/app/api.md) : `GET /movies`
- [Get Movie](/app/api.md) : `GET /movies/:mid`

## Cache

`redis` is utilized as the in-memory database.Cache aside strategy is applied in order to cache the movies.

## Tests

`pytest` is utilized for the testing. Start the local test with the following command:

```bash
sh ./test-local.sh
```

You can also test with your local virtual environment. `ENV` variables are set within the `conftest.py`, please
be aware to install `redis` on your local machine.

```console
pytest -v
```

#### Project Structure

```
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── api.md
│   ├── index.py
│   └── movies.py
├── app.py
├── docker-compose.yml
├── requirements.txt
├── services
│   ├── __init__.py
│   └── ghibli_service.py
├── static
│   ├── errors.css
│   └── style.css
├── templates
│   ├── 404.html
│   ├── 429.html
│   ├── 500.html
│   ├── base.html
│   ├── get_film.html
│   ├── index.html
│   └── list_films.html
├── test-local.sh
├── tests
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── test_index.py
│   │   └── test_movies.py
│   ├── conftest.py
│   ├── services
│   │   ├── __init__.py
│   │   └── test_ghibli_api.py
│   └── tests-start.sh
└── utils
    ├── __init__.py
    ├── cache.py
    └── error.py
```
