import pytest
import allure
import requests
from playwright.sync_api import Page
from allure_commons.types import Severity
from utils.data import FormData as fd


target_url = 'https://pentest-ground.com:81'


@pytest.mark.security
@allure.severity(Severity.NORMAL)
@allure.title("WSTG-INPV-17 - Testing for Host Header Injection")
@allure.description("Testing for Host Header Injection")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/07-input_validation_testing/17-testing_for_host_header_injection", name="Testing for Host Header Injection (WSTG-INPV-17)")    
class TestHostHeaderInjection:
    def test_HHI_web_cache_poisoning(self, page: Page):
        session = requests.Session()
        session.headers.update({
            'Host': 'https://pentest-ground.com:4280/',
            })
        response = session.get(target_url)
        assert response.status_code != 302, 'Error: {0}'.format(response.status_code)
        session.close()
    
    def test_HHI_add_XForwarded_host_parameter(self, page: Page):
        session = requests.Session()
        session.headers.update({
            'Host': f'{target_url}',
            'X-Forwarded-Host': 'www.attacker.com'
            })
        response = session.get(target_url)
        assert response.status_code != 302, 'Error: {0}'.format(response.status_code)
        session.close() 
    
    def test_HHI_by_swapping_real_host_and_XForwarded_host(self, page: Page):
        session = requests.Session()
        session.headers.update({
            'Host': 'https://www.attacker.com',
            'X-Forwarded-Host': f'{target_url}'
            })
        response = session.get(target_url)
        assert response.status_code != 302, 'Error: {0}'.format(response.status_code)
        session.close() 
    
    def test_HHI_by_adding_two_host_parameters(self, page: Page):
        session = requests.Session()
        session.headers.update({
            'Host': f'{target_url}',
            'Host': 'https://www.attacker.com',
            })
        response = session.get(target_url)
        assert response.status_code != 302, 'Error: {0}'.format(response.status_code)
        session.close()
    
    def test_HHI_by_adding_the_target_values_in_front_of_the_original_values(self, page: Page):
        session = requests.Session()
        session.headers.update({
            'Host': f'https://www.attacker.com?={target_url}'
            })
        response = session.get(target_url)
        assert response.status_code != 302, 'Error: {0}'.format(response.status_code)
        session.close()

    def test_HHI_by_adding_the_target_with_a_slash_after_the_original_values(self, page: Page):
        session = requests.Session()
        session.headers.update({
            'Host': f'https://www.attacker.com/{target_url}'
            })
        response = session.get(target_url)
        assert response.status_code != 302, 'Error: {0}'.format(response.status_code)
        session.close()
    
    def test_HHI_with_other_injections_on_the_host_parameter(self, page: Page):
        session = requests.Session()
        session.headers.update({
            'Host': f'{target_url}/dashboard',
            'BearerToken': fd.token
            })
        response = session.get(target_url)
        assert response.status_code != 302, 'Error: {0}'.format(response.status_code)
        session.close() 

    def test_HHI_by_password_reset_poisoning(self, page: Page):
        pass
    
    def test_HHI_by_accessing_private_virtual_host(self, page: Page):
        url = target_url.removeprefix('https://')
        intranet_url = 'intranet.'+url
        session = requests.Session()
        session.headers.update({
            'Host': intranet_url,
            })
        response = session.get(target_url)
        assert response.status_code != 302, 'Error: {0}'.format(response.status_code)
        session.close()