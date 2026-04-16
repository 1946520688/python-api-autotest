import json
from config import LOGIN_URL
from utils.request_util import post
from utils.assert_util import assert_status_code

def load_test_data():
    with open("data/test_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def test_login_success():
    data = load_test_data()["login_success"]
    response = post(LOGIN_URL, data)
    assert_status_code(response, 200)

def test_login_fail():
    data = load_test_data()["login_fail"]
    response = post(LOGIN_URL, data)
    assert response.status_code in [400, 401]
