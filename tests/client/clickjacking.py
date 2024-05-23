import pytest
import webbrowser
import allure
from allure_commons.types import Severity


@pytest.mark.security
@allure.severity(Severity.NORMAL)
@allure.title("WSTG-CLNT-09 - Testing for Clickjacking")
@allure.description("Script opens https://clickjacker.io/ and displays clickjacking vulnerabilty report")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/11-client-side_testing/09-testing_for_clickjacking")
class TestClickjackingVulnerability:  
    def test_run_check_for_clickjacking(self):
        with allure.step("Visit site and check for clickjacking vulnerabilities"):
            target_url = input("Please enter the URL to test: ")
            webbrowser.open_new_tab(f"https://clickjacker.io/test?url=https://{target_url}")