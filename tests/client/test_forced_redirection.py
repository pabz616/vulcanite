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
}

# src: https://swisskyrepo.github.io/PayloadsAllTheThings/Open%20Redirect/#filter-bypass


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

    def test_for_forced_redirection_with_filter_bypass(self, page: Page, target_url):
        with allure.step("Visit site and attempt forced browsing using a whitelisted domain or keyword"):
            page.goto(target_url)
            response = requests.get(target_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {target_url}"

@pytest.mark.security
@allure.severity(Severity.CRITICAL)
@allure.title("WSTG-CLNT-04 - Testing for Client-side URL Redirect )")
@allure.description("Test for forced browsing by enumerating and accessing resources that are not referenced by the application.")
class TestForcedUrlRedirect:
    def test_for_forced_redirection_using_CRLF(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using CRLF to bypass 'javascript' blacklisted keyword"):
            redir_url = pd.target_url+'evil.com'
            page.goto(redir_url + '?#redirect=java%0d%0ascript%0d%0a:alert(0)')
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url }"
            
    def test_for_forced_redirection_using_https_to_bypass_blacklisted_keywords(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using 'https:' to bypass '//' blacklisted keyword"):
            redir_url = pd.target_url+'?#redirect=https:google.com'
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_forward_slash_and_back_slash(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using '\/\/' to bypass '//' blacklisted keyword (Browsers see \/\/ as //)"):
            redir_url = pd.target_url+'?#redirect=https:\/\/google.com/'
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_encoding_to_bypass_blacklisted_character(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using '%E3%80%82' to bypass '.' blacklisted character"):
            redir_url = pd.target_url+'?#redirect=https://google%E3%80%82com'
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_null_byte(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using null byte '%00' to bypass blacklist filter"):
            redir_url = pd.target_url+'?#redirect=https://google%00.com'
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_parameter_pollution(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using parameter pollution"):
            redir_url = pd.target_url+'?next=yahoo.com&next=google.com'
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_at_symbol(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using '@' character, browser will redirect to anything after the '@' "):
            redir_url = pd.target_url+'@google.com'
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_attempting_to_create_a_directory(self, page: Page):
        with allure.step("Visit site and attempt forced browsing creating folder as their domain"):
            redir_url = 'https://www.yahoo.com/'+pd.target_url
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_question_mark(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using '?' character, browser will translate it to '/?' "):
            redir_url = 'https://www.vulnhub.com?downloads/'+pd.target_url
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_host_split_unicode_normalization(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using host/split unicode normalization"):
            redir_url = f"https://evil.c℀.{pd.target_url}"
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_xss_from_open_url(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using xss from open url"):
            redir_url = f"https://{pd.target_url};alert(0);//"
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_xss_from_data_wrapper(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using XSS from data:// wrapper"):
            redir_url = f"https://{pd.target_url};/redirect.php?url=data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik7PC9zY3JpcHQ+Cg=="
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"
            
    def test_for_forced_redirection_using_xss_from_javascript_wrapper(self, page: Page):
        with allure.step("Visit site and attempt forced browsing using XSS from javascript wrapper"):
            redir_url = f"https://{pd.target_url}/redirect.php?url=javascript:prompt(1)"
            page.goto(redir_url)
            response = requests.get(redir_url)
            assert response.status_code != 302, f"Forced browse vulnerability occurred: - {redir_url}"