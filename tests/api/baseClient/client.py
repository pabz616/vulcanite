from utils.data import APIData as api


class ApiHeaders:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        
        self.user_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': api.user_authorization
        }
        
        self.auth_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': api.admin_authorization
        }