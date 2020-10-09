def test_movies(client):
    response = client.get('/movies')
    assert response.status == '200 OK'
