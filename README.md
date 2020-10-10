## Installation
First and foremost `docker` and  `docker-compose` should be installed on your local machine.

The following commands will run the `Flask` application on `http://localhost:8000`.
```console
docker-compose build
docker-compose up -d
```

## API Documentation

API provides movie listing logic along with the index page content.
* [Index](/app/api.md): `GET /`
* [Get Movies](/app/api.md) : `GET /movies`
* [Get Movie](/app/api.md) : `GET /movie/:mid`

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