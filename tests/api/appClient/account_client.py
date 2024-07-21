from json import dumps
from api.baseClient.client import BaseClient
from utils.data import APIData as api
from utils.urls import Endpoints
from api.baseAPI.request import APIRequest


class AccountClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.account_url = Endpoints.ACCOUNT
        self.account_search_url = Endpoints.ACCOUNT_SEARCH
        self.request = APIRequest()
        