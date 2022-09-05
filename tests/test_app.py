from hello import app


def test_hello():
    response = app.test_client().get('/hello')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'
