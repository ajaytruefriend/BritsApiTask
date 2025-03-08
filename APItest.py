import requests


def test_patch():
    # Base URL of the API
    base_url = "https://api.restful-api.dev"

    # Resource
    resource = "objects"

    # Id(query_parameter)
    query_param = "ff808181932badb6019571dfd64b1563"

    # Data to send in the PATCH request (as a dictionary)
    patch_data = {
        "name": "Brits update Test1"
    }

    # Headers (if needed, e.g., for authentication)
    headers = {
        "Content-Type": "application/json"
    }

    # Perform the PATCH request
    response = requests.patch(
        f"{base_url}/{resource}/{query_param}",  # Construct the full URL
        json=patch_data,  # Send data as JSON
        headers=headers   # Include headers
    )

    # Print the response details
    print(f"PATCH Response Status Code: {response.status_code}")
    print(f"PATCH Response Body: {response.json()}")

    # Compare status code
    assert response.status_code == 200, f"TC Failed: status code expected is '200' but got {response.status_code}"
    print("TC Passed: patch request successful")

    #Compare change
    assert response.json()["name"] == "Brits update Test1", f"TC Failed: updated name is {response.json()['name']} but expected name is 'Brits update Test1'"
    print("TC Passed: name got updated correctly")


test_patch()