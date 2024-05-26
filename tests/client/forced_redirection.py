import pytest
import requests
from playwright.sync_api import Page
import utils.assertions as confirm
from utils.data import ProjectData as pd
from utils.injection_parameters import InjectionParameters as IP
import allure
from allure_commons.types import Severity

injection_params = IP.select_injection_parameters()
Url = pd.target_url

DIR = {
    f"{Url}/system/",
    f"{Url}/password/",
    f"{Url}/logs/",
    f"{Url}/admin",
    f"{Url}/test/",
    f"{Url}/dashboard",
    f"{Url}/../../../etc/passwd/"
    f"{Url}/users/",
    f"{Url}/site_map.xml",
    f"{Url}/robots.txt",
}


@pytest.mark.security
@allure.severity(Severity.CRITICAL)
@allure.title("WSTG-ATHN-04 - Testing for Bypassing Authentication Schema (Forced Browsing)")
@allure.description("Test for forced browsing by enumerating and accessing resources that are not referenced by the application.")
@allure.link("https://owasp.org/www-community/attacks/Forced_browsing", name="Test for forced browsing")    
@pytest.mark.parametrize("target_url", DIR)
class TestForcedBrowsing:
    def test_for_forced_browsing_via_static_directory_and_file_enumeration(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced browsing to a directory not explicitly visible, but available"):
            page.goto(target_url)
            response = requests.get(target_url)
            confirm.not_found_response_status(response, 404), f"Forced browse vulnerability occurred: - {target_url}"

# TODO - Add more tests as project needs warrant - example: guessng a user's id as part of url generation