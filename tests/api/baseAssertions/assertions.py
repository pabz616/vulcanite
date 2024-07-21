from assertpy import assert_that
from utils.data import ProjectData as pd
import requests


def ok_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.ok), 'Error: {0}'.format(response.status_code)
 
    
def validation_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.bad_request), 'Error: {0}'.format(response.status_code)
    

def not_found_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.not_found), 'Error: {0}'.format(response.status_code)
    
    
def bad_request_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.bad_request), 'Error: {0}'.format(response.status_code)
    
    
def entity_too_large_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.content_too_large), 'Error: {0}'.format(response.status_code)


def created_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.created), 'Error: {0}'.format(response.status_code)


def unauthorized_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.unauthorized), 'Error: {0}'.format(response.status_code)
  
    
def not_acceptable_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.not_acceptable), 'Error: {0}'.format(response.status_code)
    
    
def internal_server_error(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.internal_server_error), 'Error: {0}'.format(response.status_code)

    
def api_response_time(response):
    assert_that(response.elapsed.total_seconds()).is_less_than(pd.response_limit), "API Response: {0}".format(response.elapsed.total_seconds)
    
    
def created_token(resp_body):
    assert_that(resp_body["Authorization"]).is_not_none(), "Token was not generated"
    assert_that(resp_body["status"]).is_equal_to("success"), "Not successful"