## Installation


```console
docker-compose build
docker-compose up -d
```

## API Documentation

API provides movie listing logic along with the index page content.
* [Index](/app/api.md): `GET /`
* [Get Movies](/app/api.md) : `GET /movies`

## Cache
`redis` was utilized for the cache aside strategy.

## Tests
`pytest` was utilized for the testing. `ENV` variables 
are set within the `conftest.py`, please 
be aware to install `redis` on your local machine.
```console
pytest -v
```