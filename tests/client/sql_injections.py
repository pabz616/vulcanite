import pytest
import requests
from playwright.sync_api import Page
from utils.data import ProjectData as pd, SQLIPayloads as sqli
import utils.assertions as confirm
from tests.pages.searchPage import SearchInput as search
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
            confirm.internal_server_error(response, 500)
    
    def test_SQL_Injection_In_URL_Using_NullBytes(self, page: Page):
        with allure.step(f"Visit site and submit sql injection with null bytes in url for blog post 1  - {sqli.sqlInjection_nullBytes}"):
            attack_url = pd.target_url + '/post/1&' + sqli.sqlInjection_nullBytes
            page.goto(attack_url)
            response = requests.get(attack_url)
            confirm.bad_request_status(response, 400)
 
 
class TestSQLInjectionInSearch:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(pd.target_url)
        yield
        
    def test_SQL_Injection_With_OR_Statement_In_Search_Input(self, page: Page):
        with allure.step(f"Visit site and submit sql injection with OR statement in search input  - {sqli.sqlInjection}"):
            search(page).submit_exploit(sqli.sqlInjection)
            response = requests.get(pd.target_url)
            confirm.ok_response_status(response, 200)
            
    def test_SQL_Injection_With_Spacing_In_Search_Input(self, page: Page):
        with allure.step(f"Visit site and submit sql injection with OR statement in search input  - {sqli.sqlInjection2}"):
            search(page).submit_exploit(sqli.sqlInjection2)
            response = requests.get(pd.target_url)
            confirm.ok_response_status(response, 200)
    
    def test_SQL_Injection_With_Null_Bytes_In_Search_Input(self, page: Page):
        with allure.step(f"Visit site and submit sql injection with null bytes in search input  - {sqli.sqlInjection_nullBytes}"):
            search(page).submit_exploit(sqli.sqlInjection_nullBytes)
            response = requests.get(pd.target_url)
            confirm.ok_response_status(response, 200)  # no effect from successful injection
         
    def test_SQL_Injection_With_Encoded_String_In_Search_Input(self, page: Page):
        with allure.step(f"Visit site and submit sql injection with encoding in search input  - {sqli.sqlInjection_encoded}"):
            search(page).submit_exploit(sqli.sqlInjection_encoded)
            response = requests.get(pd.target_url)
            confirm.ok_response_status(response, 200)  # no effect from successful injection
            
    def test_SQL_Injection_With_Inline_String_In_Search_Input(self, page: Page):
        with allure.step(f"Visit site and submit sql injection with encoding in search input  - {sqli.sqlInjection_inline}"):
            search(page).submit_exploit(sqli.sqlInjection_inline)
            response = requests.get(pd.target_url)
            confirm.ok_response_status(response, 200)  # no effect from successful injection


class TestSQLInjectionAtLogin:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(pd.target_url+'/login')
        yield
                
    def test_SQL_Injection_At_Login_Username(self, page: Page):
        """Test SQL injection in query parameter should fail"""
        

#     def test_SQL_Injection_At_Login_Password(self, page: Page):
#         """Test SQL injection at password should fail"""
        
#         onBookStoreLogin = BookStoreLogin(page)
#         onBookStoreLogin.submitLogin(DemoQA.usn, pd.sqlInjection)
#         onBookStoreLogin.confirmInvalidLoginCredentialsValidation
    
#     def test_SQL_Injection_using_NULL_BYTE(self, page: Page):
#         """Test SQL injection employing a Null Byte at password should fail"""
        
#         onBookStoreLogin = BookStoreLogin(page)
#         onBookStoreLogin.submitLogin(DemoQA.usn, 'password/%')
#         onBookStoreLogin.confirmInvalidLoginCredentialsValidation
        
#     def test_SQL_Injection_with_URL_ENCODED_STRING_At_Login(self, page: Page):
#         """Test SQL injection using URL ENCODING at login should fail"""
        
#         onBookStoreLogin = BookStoreLogin(page)
#         onBookStoreLogin.submitLogin(DemoQA.usn, pd.sqlInjection_endcoded)
#         onBookStoreLogin.confirmInvalidLoginCredentialsValidation
        
#     def test_SQL_Injection_with_LOWERCASE_PAYLOAD_At_Login(self, page: Page):
#         """Test SQL injection using URL ENCODING at login should fail"""
        
#         onBookStoreLogin = BookStoreLogin(page)
#         onBookStoreLogin.submitLogin(DemoQA.usn, pd.sqlInjection_lowercase)
#         onBookStoreLogin.confirmInvalidLoginCredentialsValidation


# @pytest.mark.security
# class TestSQLInjectionAtRegistration:
#     @pytest.fixture(scope="function", autouse=True)
#     def before_each(self, page: Page):
#         page.goto(DemoQA.baseUrl+'/register')
#         yield

#     def test_SQL_Injection_At_Registration(self, page: Page):
#         """Test that bookstore validation occurs if user exists"""
#         onBookStoreRegistrationPage = Registration(page)

#         first_name = 'tester1'
#         last_name = 'tester1'
#         username = 'tester1' + pd.sqlInjection2 + '*@example.com'
#         password = 'Password123!'
       
#         onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
#         onBookStoreRegistrationPage.confirmErrorMessageForexisting_userIsDisplayed
        
#     def test_SQL_Injection_using_NULL_BYTE_At_Registration(self, page: Page):
#         """Test that registration fails when a sql injection using a null byte is attempted"""
#         onBookStoreRegistrationPage = Registration(page)

#         first_name = 'hack%00'
#         last_name = 'hack\x00'
#         username = 'tester1' + pd.sqlInjection2 + '*@example.com'
#         password = 'Password123!'
       
#         onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
#         onBookStoreRegistrationPage.confirmErrorMessageForexisting_userIsDisplayed