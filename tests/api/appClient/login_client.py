from json import dumps
from api.baseClient.client import BaseClient
from utils.data import APIData as api
from utils.urls import Endpoints
from api.baseAPI.request import APIRequest

from faker import Faker
fake = Faker()


class LoginClient(BaseClient):
    def __init__(self):
        super().__init__()        
        self.login_url = Endpoints.LOGIN
        self.request = APIRequest()
        
    def authenticate_user(self):
        payload = dumps(api.loginData)
        return self.request.post(self.login_url, payload, self.headers)
    
    def submit_blank_credentials(self):
        payload = dumps({"userName": '', "password": ''})
        return self.request.post(self.user_url, payload, self.headers)
    
    def submit_invalid_credentials(self):
        payload = dumps({"userName": fake.email(), "password": fake.pystr()})
        return self.request.post(self.login_url, payload, self.headers)
    
    def invalid_login_sqli_check(self):
        payload = dumps({"userName": 'admin', "password": 'OR 1=1--'})
        return self.request.post(self.login_url, payload, self.headers)
    
    def invalid_login_xss_check(self):
        payload = dumps({"userName": 'admin+(<script>alert(document.cookie)</script>)@example.com', "password": 'admin'})
        return self.request.post(self.login_url, payload, self.headers)
        
    def get_auth_token(self):
        payload = dumps(api.loginData)
        self.request.post(self.login_url, payload, self.user_headers)