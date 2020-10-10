import requests


def test_list_movies(client):
    response = client.get('/movies')
    assert response.status == '200 OK'


def test_get_movie(client):
    response = requests.get(f'{client.application.config["GHIBLI_URL"]}/films').json()
    assert isinstance(response, list)
    response = client.get(f'/movies/{response[0]["id"]}')
    assert response.status == '200 OK'
