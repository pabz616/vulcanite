import pytest
import requests
from playwright.sync_api import Page
from utils.data import ProjectData as pd
import utils.assertions as confirm

import allure
from allure_commons.types import Severity


Url = pd.target_url

PAGES = {
    f"{Url}about",
    f"{Url}services",
    f"{Url}blog",
    f"{Url}post/1",
    f"{Url}post/2",
    f"{Url}contact"
    f"{Url}login"
}


@pytest.mark.security
@allure.severity(Severity.NORMAL)
@allure.title("WSTG-CONF-08- Test RIA Cross Domain Policy")
@allure.description("Test for RIA Policy Files Weakness")
@allure.link("https://pentest.y-security.de/Web%20Security%20Testing%20Guide/2021/02-Configuration_and_Deployment_Management_Testing/08-Test_RIA_Cross_Domain_Policy/", name="Test RIA Cross Domain Policy (WSTG-CONF-08)")    
@pytest.mark.parametrize("target_url", PAGES)
class TestCrossDomainPolicyt:
    def test_search_for_crossdomain_file(self, page: Page, target_url):
        with allure.step("Visit site and append crossdomain.xml"):
            crossdomain_url = target_url+"/crossdomain.xml"
            page.goto(crossdomain_url)
            
        with allure.step("If found, attempt to exploit by testing for least privilege"):
            response = requests.get(crossdomain_url)
            confirm.not_found_response_status(response, 404), f"Cross Domain XML File found at: {crossdomain_url}"

    def test_search_for_client_access_policy_file(self, page: Page, target_url):
        with allure.step("Visit site and clientaccesspolicy.xml to url"):
            client_access_policy_url = target_url+"/clientaccesspolicy.xml"
            page.goto(client_access_policy_url)
            
        with allure.step("If found, attempt to exploit by testing for least privilege"):
            response = requests.get(client_access_policy_url)
            confirm.not_found_response_status(response, 404), f"Cross Domain XML File found at: {client_access_policy_url}"