def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected status code {expected_code}, but got {response.status_code}"

def assert_response_contains(response, key, expected_value):
    json_data = response.json()
    assert key in json_data, f"Key '{key}' not found in response"
    assert json_data[key] == expected_value, \
        f"Expected {key} to be '{expected_value}', but got '{json_data[key]}'"