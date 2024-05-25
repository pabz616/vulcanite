from playwright.sync_api import expect
from utils.data import SQLIPayloads as sqli

"""
LOCATORS
"""

USN = '//input[@id="form2Example1"]'
PWD = '//input[@id="form2Example2"]'
SUBMIT = '//button[contains(@class,"mb-4")]'
FORGOT_PWD_LINK = '//a[contains(.,"Forgot password?")]'
REMEMBER_ME = '//label[@for="form2Example31"]'
REGISTER = '//a[contains(.,"Register")]'
VALIDATION_MESSAGE = '//div[@class="alert alert-danger"]'

payloads = [
    sqli.sqlInjection,
    sqli.sqlInjection2,
    sqli.sqlInjection3,
    sqli.sqlInjection_encoded,
    sqli.sqlInjection_inline,
    sqli.sqlInjection_lowercase,
    sqli.sqlInjection_nullBytes
]


class LoginInput:
    def __init__(self, page):
        self.page = page

# LOGIN FORM
        self.usernameField = page.locator(f"xpath={USN}")
        self.passwordField = page.locator(f"xpath={PWD}")
        self.loginButton = page.locator(f"xpath={SUBMIT}")
        self.alertMessage = page.locator(f"xpath={VALIDATION_MESSAGE}")
    
    # FORGOT PASSWORD
        self.forgotPasswordLink = page.locator(f"xpath={FORGOT_PWD_LINK }")
        
    # REMEMBER ME
        self.rememberMeButton = page.locator(f"xpath={REMEMBER_ME}")
    
    # REGISTER
        self.registerLink = page.locator(f"xpath={REGISTER}")
    
    def navigate_to_registration_form(self):
        expect(self.registerLink).to_be_visible()
        self.registerLink.click()
    
    def submit_exploit_in_username_field(self):
        for exploit in payloads:
            self.usernameField.fill(f"admin {exploit}")
            self.passwordField.fill('qwerty')
            self.loginButton.click()

    def submit_exploit_in_password_field(self):
        for exploit in payloads:
            self.usernameField.fill('admin')
            self.passwordField.fill(exploit)
            self.loginButton.click()
        
    def confirm_validation_occurred(self):
        expect(self.alertMessage).to_be_visible()
        
    def confirm_no_alert_present(self):
        assert self.alert is None