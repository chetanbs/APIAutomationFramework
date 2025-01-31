# Reason : To reuse the Create token and Create Booking.
from enum import verify
from http.client import responses

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

import allure
import pytest

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url = APIConstants().url_create_token(),
        headers = Utils().common_headers_json(),
        auth = None,
        payload = payload_create_token(),
        in_json = False
    )
    print(response.json())
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_not_none(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def create_booking_id():
    response = post_request(
        url=APIConstants().url_create_booking(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_booking(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expected_data=200)
    booking_id = response.json()["bookingid"]
    verify_json_key_not_null(booking_id)
    print("Created")
    print(response.json())
    return booking_id


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants().url_create_booking(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_not_null(response.json()["bookingid"])
    return booking_id