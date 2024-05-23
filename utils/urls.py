import os
from utils.data import ProjectData as pd

# TODO: FILL THIS OUT DURING RECON PHASE OF PEN TESTING; REQUEST SWAGGER DOCUMENTATION

class Endpoints(object):
    RFB_URL = os.getenv("BASE_URL", pd.target_endpoint)
    BOOKINGS = f"{RFB_URL}/booking"
    RANDOM_BOOKING_ID = f"{RFB_URL}/booking/{*.booking_id}"
    SINGLE_BOOKING_ID = f"{RFB_URL}/booking/2"
    AUTH_URL = f"{RFB_URL}/auth"