import pytest
import requests
from playwright.sync_api import Page
from utils.data import ProjectData as pd
from utils.injection_parameters import InjectionParameters as IP
import allure
from allure_commons.types import Severity

file_path = '../../utils/ssrf_payloads.txt'


# PAYLOAD FILE
with open(file_path) as file:
    payload = file.read()
    
# INJECTION PARAMETERS
injection_params = IP.select_injection_parameters()      
Url = pd.target_url

PAGES = {
    f"{Url}/about",
    f"{Url}/services",
    f"{Url}/blog",
    f"{Url}/post/1",
    f"{Url}/post/2",
    f"{Url}/contact"
    f"{Url}/login"
}


@pytest.mark.security
@allure.severity(Severity.CRITICAL)
@allure.title("WSTG-INPV-19 - Testing for Server-Side Request Forgery")
@allure.description("Test if the injection points are exploitable")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/07-input_validation_testing/19-testing_for_server-side_request_forgery", name="Testing for Server-Side Request Forgery (WSTG-INPV-19)")    
@pytest.mark.parametrize("target_url", PAGES)
class TestServerSideRequestForgery:
    def test_ssrf_whitelisted_domain_bypass(self, page: Page, target_url):
        with allure.step("Visit site and attempt to bypass whitelisted domains"):
            ssrf_bypassed_url = target_url+f"{injection_params}"
            page.goto(ssrf_bypassed_url)
            response = requests.get(ssrf_bypassed_url)
            assert response.status_code != 302,  f"Vulnerability found! Whitelist bypassed with {ssrf_bypassed_url} was successful"

    @pytest.mark.skip(reason="Unskip as the need warrants")            
    def test_ssrf_with_dot_bypass(self, page: Page, target_url):
        with allure.step("Visit site and attempt to use dot bypass url schema"):
            ssrf_url = '127%E3%80%820%E3%80%820%E3%80%821?'+target_url
            page.goto(ssrf_url)
            response = requests.get(ssrf_url)
            assert response.status_code != 302,  f"Vulnerability found! Whitelist bypassed with {ssrf_url} was successful"

    @pytest.mark.skip(reason="Unskip as the need warrants")
    def test_ssrf_with_add_0_bypass(self, page: Page, target_url):
        with allure.step("Visit site and attempt to use add zero (0) bypass url schema"):
            ssrf_url = '127.000000000000.1/'+target_url
            page.goto(ssrf_url)
            response = requests.get(ssrf_url)
            assert response.status_code != 302,  f"Vulnerability found! Whitelist bypassed with {ssrf_url} was successful"

    def test_ssrf_with_file_protocol(self, page: Page, target_url):
        with allure.step("Visit site and attempt to use The URL scheme file://"):
            ssrf_url = target_url+'?file:///////etc/passwd'
            page.goto(ssrf_url)
            response = requests.get(ssrf_url)
            assert response.status_code != 302,  f"Vulnerability found! Whitelist bypassed with {ssrf_url} was successful"
            
    def test_ssrf_with_domain_confusion(self, page: Page, target_url):
        with allure.step("Visit site and attempt to employ domain-confusion url schema"):
            ssrf_url = 'https://attacker.com:\@@'+target_url
            page.goto(ssrf_url)
            response = requests.get(ssrf_url)
            assert response.status_code != 302,  f"Vulnerability found! Whitelist bypassed with {ssrf_url} was successful"

    @pytest.mark.skip(reason="Unskip as the need warrants")
    def test_ssrf_with_malformed_url(self, page: Page, target_url):
        with allure.step("Visit site and attempt to employ malformed url schema"):
            ssrf_url = 'localhost:+11211aaa?'+target_url
            page.goto(ssrf_url)
            response = requests.get(ssrf_url)
            assert response.status_code != 302,  f"Vulnerability found! Whitelist bypassed with {ssrf_url} was successful"