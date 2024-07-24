"""
TEST LOGIN ENDPOINT
 """
    
import pytest
import json
from api.appClient.login_client import LoginClient
from api.baseAssertions.assertions import assertions as confirm


client = LoginClient()


@pytest.mark.critical
@pytest.mark.api
class TestCriticalLoginEndpoint:
    def test_login(self):
        response = client.authenticate_user()
        confirm.ok_response_status(response, 200)
        confirm.api_response_time
        
    def test_blank_login(self):
        response = client.submit_blank_credentials()
        confirm.validation_response_status(response, 400)
        
    def test_invalid_login(self):
        response = client.submit_invalid_credentials()
        confirm.validation_response_status(response, 400)
        
    def test_invalid_login_sqli_check(self):
        response = client.invalid_login_sqli_check()
        confirm.validation_response_status(response, 400)
        
    def test_invalid_login_xss_check(self):
        response = client.invalid_login_xss_check()
        confirm.validation_response_status(response, 400)
        
    def test_get_token(self):
        response = client.authenticate_user()
        data = json.loads(response.text)
        confirm.ok_response_status(response, 200)
        confirm.created_token(data)