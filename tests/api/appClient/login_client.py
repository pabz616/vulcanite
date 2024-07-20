from 
from utils.api_requests import APIRequest
import requests
from utils.data import ProjectData as pd

session = requests.Session()


class APIClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.request = APIRequest()
        self.target_url = pd.target_url
                
    def update_header(self, host):
        session.headers.update({
            'Host': f"{host}"
        })
        return self.request.put(self.target_url, self.headers)
    
    session.close()