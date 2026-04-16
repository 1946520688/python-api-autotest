import json
from config import REGISTER_URL
from utils.request_util import post
from utils.assert_util import assert_status_code

def load_test_data():
    with open("data/test_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def test_register():
    data = load_test_data()["register_data"]
    response = post(REGISTER_URL, data)
    assert_status_code(response, 200)
