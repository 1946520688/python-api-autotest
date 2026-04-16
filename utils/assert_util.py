def assert_status_code(response, expected_code):
    assert response.status_code == expected_code

def assert_response_contains(response, key):
    assert key in response.text
