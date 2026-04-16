from config import USER_INFO_URL
from utils.request_util import get
from utils.assert_util import assert_status_code

def test_get_user_info():
    headers = {
        "Authorization": "Bearer test_token"
    }
    response = get(USER_INFO_URL, headers=headers)
    assert_status_code(response, 200)
