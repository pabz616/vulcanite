import requests
import pytest

# Replace these with appropriate values for your application
BASE_URL = "http://yourapp.com"
VALID_USER_ID = "123"
INVALID_USER_ID = "456"
USER_AUTH_TOKEN = "valid_user_token"  # The auth token for a user with user_id=123


@pytest.fixture
def auth_headers():
    return {
        "Authorization": f"Bearer {USER_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }


def test_indirect_object_reference(auth_headers):
    # Valid request by the user to their own resource
    valid_url = f"{BASE_URL}/user/{VALID_USER_ID}"
    response = requests.get(valid_url, headers=auth_headers)
    assert response.status_code == 200, f"Expected 200 OK but got {response.status_code}"
    
    # Attempt to access another user's resource
    invalid_url = f"{BASE_URL}/user/{INVALID_USER_ID}"
    response = requests.get(invalid_url, headers=auth_headers)
    
    # Depending on your application's response to unauthorized access,
    # you might expect a 403 Forbidden, 404 Not Found, etc.
    assert response.status_code in {403, 404}, f"Expected 403 or 404 but got {response.status_code}"


if __name__ == "__main__":
    pytest.main()
