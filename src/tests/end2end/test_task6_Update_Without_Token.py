# Try to update without the token

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import patch_requests
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class Test_update_WO_token(object):
    def test_update_wo_token(self, create_booking_id):
        booking_id = create_booking_id
        token = " "
        update_url = APIConstants.url_patch_put_delete(booking_id)
        response = patch_requests(
            url=update_url,
            auth=None,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking_patch(),
            in_json=False
        )
        print(update_url)
        print(Utils().common_header_put_delete_patch_cookie(token=token))
        verify_http_status_code(response_data=response, expected_data=403)
        verify_response_update_WO_token(response=response.text)