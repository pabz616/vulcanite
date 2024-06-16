from utils.data import ProjectData as pd


class BaseClient:
    def __init__(self):
        self.headers = {
            'Host': pd.target_endpoint,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        
    def create_headers(host, xFwdHost):
        return {
            'Host': f'{host}',
            'X-Forwarded-Host': f'{xFwdHost}'
        }
        