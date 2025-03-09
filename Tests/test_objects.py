import pytest

from Utils.api_client import APIClient
from Utils.assertions import assert_status_code, assert_response_contains



def test_patch_object(api_client):
    # Data to send in the PATCH request
    patch_data = {
        "name": "Brits update Test22"
    }

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    # Perform the PATCH request
    response = api_client.patch(patch_data, headers=headers)

    # Print the response details
    print(f"PATCH Response Status Code: {response.status_code}")
    print(f"PATCH Response Body: {response.json()}")

    # Assertions
    assert_status_code(response, 200)
    assert_response_contains(response, "name", "Brits update Test22")