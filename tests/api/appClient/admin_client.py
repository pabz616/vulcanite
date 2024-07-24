from json import dumps
from api.baseClient.client import BaseClient
from utils.urls import Endpoints
from api.baseAPI.request import APIRequest

from faker import Faker
fake = Faker()


class AdminClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.admin_create_user = Endpoints.ADMIN_ADD_USER
        self.admin_change_password = Endpoints.ADMIN_CHANGE_PASSWORD
        self.request = APIRequest()
        
    def create_user(self):
        payload = dumps({
            "firstname": "Bilbo",
            "lastname": "Baggiins",
            "username": "bilbob",
            "password1": "S3l3ctS0methingStr0ng5AsP@ssword",
            "password2": "S3l3ctS0methingStr0ng5AsP@ssword"
            })
        return self.request.post(self.admin_create_user, payload, self.admin_headers)
    
    def change_password(self):
        payload = dumps({
            "username": "bilbob",
            "password1": "Th1s!sz3nu3Passv0rd",
            "password2": "Th1s!sz3nu3Passv0rd"
            })
        return self.request.post(self.admin_change_password, payload, self.admin_headers)