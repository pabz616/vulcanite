from json import dumps
from api.baseClient.client import BaseClient
# from utils.data import APIData as api
from utils.urls import Endpoints
from api.baseAPI.request import APIRequest

account_no = 800000


class AccountClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.account_url = Endpoints.ACCOUNT
        self.request = APIRequest()
        
    def get_all_accounts(self):
        return self.request.get(self.account_url, self.user_headers)
    
    def get_account_details(self):
        return self.request.get(self.account_url+f"/{account_no}", self.admin_headers)
    
    def get_account_transactions(self):
        return self.request.get(self.account_url+f"/{account_no}/transactions", self.admin_headers)
    
    def get_transactions_by_date(self, start_date, end_date):
        payload = dumps({"startDate": start_date, "endDate": end_date})
        return self.request.get(self.account_url+f"/{account_no}/transactions", payload, self.admin_headers)