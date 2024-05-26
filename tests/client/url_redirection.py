import pytest
from playwright.sync_api import Page, expect
from utils.data import ProjectData as pd
from utils.injection_parameters import InjectionParameters as IP
import allure
from allure_commons.types import Severity

file_path = '../../utils/payload.txt'


# PAYLOAD FILE
with open(file_path) as file:
    payload = file.read()
    
# INJECTION PARAMETERS
injection_params = IP.select_injection_parameters()      
Url = pd.target_url
redirect_url = "https://www.hackthissite.org/"

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
@allure.title("WSTG-CLNT-04 - Testing for Client-side URL Redirect")
@allure.description("Test for client-side URL redirection")
@allure.link("https://owasp.boireau.io/4-web_application_security_testing/11-client-side_testing/04-testing_for_client-side_url_redirect", name="Test for client-side URL redirection (WSTG-CLNT-04)")    
@pytest.mark.parametrize("target_url", PAGES)
class TestForcedURLRedirect:
    def test_url_redirect_with_domain_parameters(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect with domain parameters"):
            forced_redirect_url = target_url+f"{injection_params}"+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(redirect_url), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
        
    def test_url_redirect_with_payload(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect with payload"):        
            forced_redirect_url = target_url+"&url="+payload
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(payload), f"Vulnerability found! Forced redirected to {payload} was successful"
        
    def test_url_redirect_with_whitelisted_word(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect with whitelisted words"):
            forced_redirection = target_url+"?image_url="+redirect_url
            page.goto(forced_redirection)
            expect(page).not_to_have_url(f"{redirect_url}"), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
        
    def test_url_redirect_with_subdomain_same_as_target(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect with subdomain as target"):
            forced_redirect_url = target_url+"."+target_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(forced_redirect_url), f"Vulnerability found! Forced redirected to {forced_redirect_url} was successful"
        
    def test_url_redirect_with_redirection_by_XSS(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using CRLF to bypass 'javascript' blacklisted keyword"):
            redirect_url = "java%0d%0ascript%0d%0a:alert(0)"
            forced_redirect_url = target_url+"?destination="+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_double_backslash_to_bypass_HTTP_blacklisted_keyword(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect with double-backslash - //"):
            redirect_url = "//google.com"
            forced_redirect_url = target_url+"?destination="+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_triple_backslash_to_bypass_HTTP_blacklisted_keyword(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using triple-backslash - ///"):
            redirect_url = "///google.com"
            forced_redirect_url = target_url+"?destination="+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_HTTPS_to_bypass_double_forward_slash(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using HTTPS to bypass double-forward slash"):
            redirect_url = "https:google.com"
            forced_redirect_url = target_url+"?destination="+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
            
    def test_url_redirect_using_escape_sequence_to_bypass_double_forward_slash(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using escape sequence to bypass double-forward slash"):
            redirect_url = "\/\/google.com/"
            forced_redirect_url = target_url+"?destination="+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_url_encoding_to_bypass_blacklisted_period_character(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using url encoding to bypass blacklisted period character"):
            redirect_url = "//google%E3%80%82com"
            forced_redirect_url = target_url+"?redir="+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
            
    def test_url_redirect_using_null_byte_to_bypass_blacklist_filter(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using null byte to bypass blacklisted filter"):
            redirect_url = "//google%00.com"
            forced_redirect_url = target_url+"?redir="+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_parameter_pollution(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using parameter pollution"):
            redirect_url = "?next=whitelisted.com&next=google.com"
            forced_redirect_url = target_url+"?redir="+redirect_url
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"{redirect_url}"), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
        
    def test_url_redirect_using_at_character(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using '@' character after redirection url"):        
            forced_redirect_url = redirect_url+"@hacker.com"
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"{forced_redirect_url}"), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
        
    def test_url_redirect_creating_folder_as_their_domain(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect by creating a folder as the domain - url_a/url_b"):    
            forced_redirect_url = f"{target_url}/{redirect_url}"
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"{redirect_url}"), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
    
    @pytest.mark.xfail(reason="page fails to load, but url loads with redirect parameter")    
    def test_url_redirect_using_xss_from_data_wrapper(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced-redirect using cross-site-script from data-wrapper"):
            forced_redirect_url = f"{target_url}/redirect.php?url=data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik7PC9zY3JpcHQ+Cg=="
            page.goto(forced_redirect_url)
            expect(page).not_to_have_url(f"{forced_redirect_url}"), f"Vulnerability found! Forced redirected to {forced_redirect_url} was successful"

