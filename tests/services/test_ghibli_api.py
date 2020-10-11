import requests


def test_ghibli_movies_api(client):
    response = requests.get(f'{client.application.config["GHIBLI_URL"]}/films').json()
    assert isinstance(response, list)


def test_ghibli_movie_api(client):
    response = requests.get(f'{client.application.config["GHIBLI_URL"]}/films').json()
    assert isinstance(response, list)
    response = requests.get(f'{client.application.config["GHIBLI_URL"]}/films/{response[0]["id"]}').json()
    assert isinstance(response, dict)
