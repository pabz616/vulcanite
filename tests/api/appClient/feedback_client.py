from json import dumps
from api.baseClient.client import BaseClient
from utils.urls import Endpoints
from api.baseAPI.request import APIRequest

feedback_id = '303030'


class FeedbackClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.submit_feedback = Endpoints.FEEDBACK_SUBMISSION
        self.view_feedback = Endpoints.FEEDBACK_VIEW
        self.request = APIRequest()
        
    def submit_feedback(self):
        payload = dumps({
            "name": "Bilbo",
            "email": "Baggiins",
            "subject": "xxxx",
            "messsage": "I like the new look of your applicaiton",
            })
        return self.request.post(self.submit_feedback, payload, self.headers)
    
    def get_feedback(self):
        return self.request.get(self.view_feedback+f"{feedback_id}", self.user_headers)
    
        