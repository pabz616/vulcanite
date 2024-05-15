import os
from utils.data import *


class Endpoints(object):
    RFB_URL = os.getenv("BASE_URL", *.restful_booker)
    BOOKINGS = f"{RFB_URL}/booking"
    RANDOM_BOOKING_ID = f"{RFB_URL}/booking/{*.booking_id}"
    SINGLE_BOOKING_ID = f"{RFB_URL}/booking/2"
    AUTH_URL = f"{RFB_URL}/auth"