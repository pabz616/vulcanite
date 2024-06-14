import pytest
import allure
from playwright.sync_api import Page
from allure_commons.types import Severity

@pytest.mark.security
@allure.severity(Severity.NORMAL)
@allure.title("WSTG-INPV-17 - Testing for Host Header Injection")
@allure.description("Testing for Host Header Injection")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/07-input_validation_testing/17-testing_for_host_header_injection", name="Testing for Host Header Injection (WSTG-INPV-17)")    
class TestHostHeaderInjection:
    def test_HHI_changed_host_parameter(self, page: Page):
        pass
    
    def test_HHI_add_XForwarded_host_parameter(self, page: Page):
        pass
    
    def test_HHI_by_swapping_real_host_and_XForwarded_host(self, page: Page):
        pass
    
    def test_HHI_by_adding_two_host_parameters(self, page: Page):
        pass
    
    def test_HHI_by_adding_the_target_values_in_front_of_the_original_values(self, page: Page):
        pass

    def test_HHI_by_adding_the_target_with_a_slash_after_the_original_values(self, page: Page):
        pass
    
    def test_HHI_with_other_injections_on_the_host_parameter(self, page: Page):
        pass     

    def test_HHI_by_password_reset_poisoning(self, page: Page):
        pass

#TODO Find a dummy python api script