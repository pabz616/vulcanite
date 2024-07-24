import os
from utils.data import APIData as api

# TODO: FILL THIS OUT DURING RECON PHASE OF PEN TESTING; REQUEST SWAGGER DOCUMENTATION


class Endpoints(object):
    BASE_URL = os.getenv("BASE_URL", api.target_endpoint)
    LOGIN = f"{BASE_URL}/login"
    ACCOUNT = f"{BASE_URL}/account"
    ACCOUNT_TRANSACTIONS = f"{BASE_URL}/account/{accountNo}/transactions"
    TRANSFER = f"{BASE_URL}/transfer"
    FEEDBACK_SUBMISSION = f"{BASE_URL}/feedback/submit"
    FEEDBACK_VIEW = f"{BASE_URL}/feedback"
    ADMIN_ADD_USER = f"{BASE_URL}/admin/addUser"
    ADMIN_CHANGE_PASSWORD = f"{BASE_URL}/admin/changePassword"
    LOGOUT = f"{BASE_URL}/logout"