import pytest
import requests
from playwright.sync_api import Page
import allure
from allure_commons.types import Severity
from utils.data import URLPayloads as urls


@pytest.mark.security
@allure.severity(Severity.CRITICAL)
@allure.title("WSTG-INPV-04 - Test For HTTP Parameter Pollution")
@allure.description("tests the applications response to receiving multiple HTTP parameters with the same name")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/07-input_validation_testing/04-testing_for_http_parameter_pollution")
def test_parameter_pollution(page: Page):
    target_url = 'https://pentest-ground.com:81/' # input("Please enter the URL to test: ")  
    with allure.step("Visit site and check for clickjacking vulnerabilities"):
        for params in urls.parameterList:
            page.goto(target_url+f"/{params}")
            response = requests.get(target_url+f"{params}")
            assert response.status_code != 302, f"Vulnerability found! Redirect was successful at {0}.format(response.status_code)"