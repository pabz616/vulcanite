import pytest
import requests
from playwright.sync_api import Page
from utils.data import URLPayloads as urls, ProjectData as pd

import allure
from allure_commons.types import Severity
from pathlib import Path



@pytest.mark.security
@allure.severity(Severity.CRITICAL)
@allure.title("WSTG-INPV-04 - Test For HTTP Parameter Pollution")
@allure.description("tests the applications response to receiving multiple HTTP parameters with the same name")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/07-input_validation_testing/04-testing_for_http_parameter_pollution")
def test_parameter_pollution(page: Page):  # input("Please enter the URL to test: ")  
    with allure.step("Visit site and check for clickjacking vulnerabilities"):
        for params in urls.parameterList:
            page.goto(pd.target_url+f"{params}")
            response = requests.get(pd.target_url+f"{params}")
            assert response.status_code != 302, f"Vulnerability found! Redirect was successful at {0}.format(response.status_code)"
            # png_bytes = page.screenshot()
            # Path("full-page.png").write_bytes(png_bytes)
            # allure.attach.file("full-page.png", name="full-page", attachment_type=allure.attachment_type.PNG)