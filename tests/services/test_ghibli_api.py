def test_ghibli_api(client):
    response = client.get('/movies')
    assert response.status == '200 OK'
