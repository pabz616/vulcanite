import pytest
from playwright.sync_api import Page
from utils.data import XSSPayloads as xss, ProjectData as pd
from tests.pages.searchPage import SearchInput as search
import allure
from allure_commons.types import Severity


@pytest.mark.security
@allure.severity(Severity.CRITICAL)
@allure.title("WSTG-INPV-01 - Test For Reflected Cross Site Scripting")
@allure.description("Ensure these characters are filtered <>’’&””")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/07-input_validation_testing/01-testing_for_reflected_cross_site_scripting")    
class TestReflectedCrossSiteScriptInjection:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(pd.target_url)
        yield

    def test_xss_using_html_tags(self, page: Page):
        with allure.step(f"Visit site, navigate to search input, and submit xss using html tag - {xss.simpleHTML}"):
            search(page).submit_exploit(xss.simpleHTML)
  
    def test_xss_using_html_entities(self, page: Page):
        with allure.step(f"Visit site, navigate to search input, and submit xss by replacing < and > with HTML entities &lt; and &gt; -  {xss.htmlEntities}"):
            search(page).submit_exploit(xss.htmlEntities)

    def test_xss_using_image_tag(self, page: Page):
        with allure.step(f"Visit site, navigate to search input, and submit xss by using an image tag - {xss.xssImageTag}"):
            search(page).submit_exploit(xss.xssImageTag)
                            
    def test_xss_with_a_character_escape_sequence(self, page: Page):
        with allure.step(f"Visit site, navigate to search input, and submit xss by using escape sequences - {xss.escapeSequence}"):
            search(page).submit_exploit(xss.escapeSequence)
                 
    def test_xss_with_lower_case_script(self, page: Page):
        with allure.step(f"Visit site, navigate to search input, and submit xss checking if case sensitive (lower case) - {xss.jsInjection}"):
            search(page).submit_exploit(xss.jsInjection)
        
    def test_xss_with_upper_case_script(self, page: Page): 
        with allure.step(f"Visit site, navigate to search input, and submit xss checking if case sensitive (upper case) - {xss.jsInjectionAllCaps}"):
            search(page).submit_exploit(xss.jsInjectionAllCaps)

    def test_xss_with_double_encoding(self, page: Page):
        with allure.step(f"Visit site, navigate to search input, and submit xss with double-encoded string - {xss.encoding}"):
            search(page).submit_exploit(xss.encoding)

    def test_xss_with_recursive_filters(self, page: Page):
        with allure.step(f"Visit site, navigate to search input, and submit xss with recursive filter - {xss.recursiveFilter}"):
            search(page).submit_exploit(xss.recursiveFilter)
        
    def test_xss_with_anchor_tags_no_whitespace(self, page: Page):
        with allure.step(f"Visit site, navigate to search input, and submit xss with anchor tags - {xss.anchorTag}"):
            search(page).submit_exploit(xss.anchorTag)