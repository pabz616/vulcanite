import requests
from utils.data import SQLIPayloads as sqli

"""
LOCATORS
""" 

EMAIL = '(//input[@type="email"])[2]'
SUBMIT = '//button[contains(.,"Subscribe")]'

payloads = [
    sqli.sqlInjection,
    sqli.sqlInjection2,
    sqli.sqlInjection3,
    sqli.sqlInjection_encoded,
    sqli.sqlInjection_inline,
    sqli.sqlInjection_lowercase,
    sqli.sqlInjection_nullBytes
]


class EmailInput:
    def __init__(self, page):
        self.page = page
        
        self.emailField = page.locator(f"xpath={EMAIL}")
        self.subscribeButton = page.locator(f"xpath={SUBMIT}")
        
    def submit_exploit_in_email_field(self):
        for exploit in payloads:
            self.emailAddressField.fill(f"test+{exploit}+@mail.com")
            self.subscribeButton.click()
            
    def confirm_form_submission_is_unsuccessful(self, url):
        response = requests.get(url)
        assert response.status_code != 302, f"SQLI InjectionVulnerability occurred using - {0}"