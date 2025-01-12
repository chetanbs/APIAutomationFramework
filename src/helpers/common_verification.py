# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# JSON Schema


# Verify HTTP Status Code
def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed to get the Status Code"


# Verify the key is as expected
def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed to match the key"


# Verify if the key value  is not null
def verify_json_key_not_null(key):
    assert key != 0, "Failed key is null"


# Verify if the key value  is not None
def verify_json_key_not_none(key):
    assert key is not None, "Failed key is none"


# Verify if key value is greater than zero
def verify_json_key_gr_zero(key):
    assert key > 0, "Failed Key is not > 0"


# Verify the response after deleting a booking id
def verify_response_delete(response):
    assert "Not Found" in response


# Verify the response while trying to update a deleted  booking id
def verify_response_update_delete(response):
    assert "Method Not Allowed" in response


# Verify the response while  updating  a booking id without entering the token
def verify_response_update_WO_token(response):
    assert "Forbidden" in response


# Verify the response text  while giving any invalid HTTP request  -Bad Request
def verify_bad_request_error(response):
    assert "Bad Request" in response
