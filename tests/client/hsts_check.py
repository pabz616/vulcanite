import pytest
from playwright.sync_api import Page
from utils.data import ProjectData as pd
import allure
from allure_commons.types import Severity
import webbrowser

TARGET_URL = pd.target_url


@pytest.mark.security
@allure.severity(Severity.NORMAL)
@allure.title("WSTG-CONF-07 - Test HTTP Strict Transport Security")
@allure.description("The presence of the HSTS header can be confirmed by examining the server's response")
@allure.link("https://owasp.boireau.io/4-web_application_security_testing/02-configuration_and_deployment_management_testing/07-test_http_strict_transport_security", name="Test HTTP Strict Transport Security (WSTG-CONF-07)")    
class TestHTTPStrictTransportSecurity:
    def test_for_HTTP_strict_transport_security(self, page: Page):
        with allure.step("Visit site and review results of report"):
            webbrowser.open(f"https://hstspreload.org/?domain={TARGET_URL}")
        pass
            
    # TODO - alt. check: run this command in terminal: curl -s -D- <target_url> | grep -i strict