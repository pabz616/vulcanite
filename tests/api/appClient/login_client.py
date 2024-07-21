from json import dumps
from api.baseClient.client import BaseClient
from utils.data import APIData as api
from utils.urls import Endpoints
from api.baseAPI.request import APIRequest


class LoginClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.login_url = Endpoints.LOGIN
        self.request = APIRequest()
        
    def authenticate_user(self):
        payload = dumps(api.loginData)
        return self.request.post(self.login_url, payload, self.headers)
    
    def submit_blank_credentials(self):
        payload = dumps(api.blankLoginData)
        return self.request.post(self.login_url, payload, self.headers)
    
    def submit_invalid_credentials(self):
        payload = dumps(api.invalidLoginData)
        return self.request.post(self.login_url, payload, self.headers)
        
    def get_auth_token(self):
        payload = dumps(api.loginData)
        self.request.post(self.login_url, payload, self.user_headers)