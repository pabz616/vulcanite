import pytest
import webbrowser
import allure
from playwright.sync_api import expect, Page
from allure_commons.types import Severity


@pytest.mark.security
@allure.severity(Severity.NORMAL)
@allure.title("WSTG-CLNT-07 - Testing Cross Origin Resource Sharing")
@allure.description("Script opens https://cors-test.codehappy.dev/ and checks for setup of CORS")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/11-client-side_testing/07-testing_cross_origin_resource_sharing", name="Test for CORS (WSTG-CLNT-07)")
class TestCrossOriginResourceSharing:  
    def test_run_check_for_cors(self, page: Page):
        with allure.step("Visit site and check for the access-control-allow-origin header; works with CORS"):
            target_url = input("Please enter the URL to test: ")
            webbrowser.open_new_tab(f"https://cors-test.codehappy.dev/?url={target_url}&origin={target_url}&method=get")
            
            cors_error = page.locator('//div[@class="Toast Toast--error mb-4"]')
            expect(cors_error).not_to_be_visible(), "Fix for CORS required"