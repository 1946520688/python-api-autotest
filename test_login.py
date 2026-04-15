import requests

def test_login():
    url = "https://example.com/api/login"
    data = {
        "username": "test_user",
        "password": "123456"
    }

    response = requests.post(url, json=data)

    assert response.status_code == 200
