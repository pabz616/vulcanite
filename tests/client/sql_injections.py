import pytest
import requests
from playwright.sync_api import Page
from utils.data import ProjectData as pd, SQLIPayloads as sqli
import utils.assertions as confirm
from tests.pages.searchPage import SearchInput as atSearch
from tests.pages.loginPage import LoginInput as atLogin
import allure
from allure_commons.types import Severity


@pytest.mark.security
@allure.severity(Severity.CRITICAL)
@allure.title("WSTG-INPV-05 - Testing for SQL Injection")
@allure.description("SQL injection testing checks if it is possible to inject data into the application so that it executes a user-controlled SQL query in the database")
@allure.link("https://owasp.boireau.io/4-web_application_security_testing/07-input_validation_testing/05-testing_for_sql_injection", name="Testing for SQL Injection (WSTG-INPV-05)")    
class TestSQLInjection:
    def test_SQL_Injection_In_URL(self, page: Page):
        with allure.step(f"Visit site and submit sql injection in url for blog post 1  - {sqli.sqlInjection2}"):
            attack_url = pd.target_url + '/post/1&' + sqli.sqlInjection2
            page.goto(attack_url)
            response = requests.get(attack_url)
            confirm.internal_server_error(response, 500), f"SQLI InjectionVulnerability occurred using - {0}"
    
    def test_SQL_Injection_In_URL_Using_NullBytes(self, page: Page):
        with allure.step(f"Visit site and submit sql injection with null bytes in url for blog post 1  - {sqli.sqlInjection_nullBytes}"):
            attack_url = pd.target_url + '/post/1&' + sqli.sqlInjection_nullBytes
            page.goto(attack_url)
            response = requests.get(attack_url)
            confirm.bad_request_status(response, 400),  f"SQLI InjectionVulnerability occurred using - {0}"
 

class TestSQLInjectionInSearch:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(pd.target_url)
        yield
        
    def test_SQL_Injection_In_Search_Input(self, page: Page):
        with allure.step("Visit site and submit sql injection in search input"):
            atSearch(page).submit_exploit
            response = requests.get(pd.target_url)
            confirm.ok_response_status(response, 200), f"SQLI InjectionVulnerability occurred using - {0}"
            
    
class TestSQLInjectionAtLogin:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(pd.target_url+'/login')
        yield
        
    def test_SQL_Injection_At_Login_Username(self, page: Page):
        with allure.step("Visit site and submit sql injection at login username input"):
            atLogin(page).submit_exploit_in_username_field
            atLogin(page).confirm_validation_occurred, f"SQLI InjectionVulnerability occurred using - {0}"
                
    def test_SQL_Injection_At_Login_Password(self, page: Page):
        with allure.step("Visit site and submit sql injection at login password input"):
            atLogin(page).submit_exploit_in_password_field
            atLogin(page).confirm_validation_occurred, f"SQLI InjectionVulnerability occurred using - {0}"
            
  
class TestSQLInjectionAtRegistration:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(pd.target_url+'/login')
        yield

    @pytest.mark.skip(reason="Not implemented")
    def test_SQL_Injection_At_Registration(self, page: Page):        
        atLogin(page).navigate_to_registration_form