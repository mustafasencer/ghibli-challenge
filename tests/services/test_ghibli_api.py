import requests


def test_ghibli_api(client):
    response = requests.get(f'{client.application.config["GHIBLI_URL"]}/films').json()
    assert isinstance(response, list)
