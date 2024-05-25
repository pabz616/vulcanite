from utils.data import SQLIPayloads as sqli, FormData as fd
import requests

"""
LOCATORS
"""
NAME = '//input[@placeholder="Your Name"]'
EMAIL = '//input[@placeholder="Email"]'
PHONE = '//input[@placeholder="Phone Number"]'
MSG = '//input[@placeholder="Message"]'
SUBMIT = '//button[contains(.,"Submit")]'

payloads = [
    sqli.sqlInjection,
    sqli.sqlInjection2,
    sqli.sqlInjection3,
    sqli.sqlInjection_encoded,
    sqli.sqlInjection_inline,
    sqli.sqlInjection_lowercase,
    sqli.sqlInjection_nullBytes
]


class ContactForm:
    def __init__(self, page):
        self.page = page
        self.nameField = page.locator(f"xpath={NAME}")
        self.emailAddressField = page.locator(f"xpath={EMAIL}")
        self.phoneNumberField = page.locator(f"xpath={PHONE}")
        self.messageField = page.locator(f"xpath={MSG}")
        self.submitButton = page.locator(f"xpath={SUBMIT}")
       
    def submit_exploit_in_name_field(self):
        for exploit in payloads:
            self.nameField.fill(fd.fname+''+f"{exploit}")
            self.emailAddressField.fill(fd.email)
            self.phoneNumberField.fill(fd.tel)
            self.messageField.fill('This is a cool automated test for SQL Injection at name input .. dont panic')
            self.submitButton.click()

    def submit_exploit_in_email_field(self):
        for exploit in payloads:
            self.nameField.fill(fd.fname+''+fd.lname)
            self.emailAddressField.fill(f"test+{exploit}+@mail.com")
            self.phoneNumberField.fill(fd.tel)
            self.messageField.fill('This is a cool automated test for SQL Injection at email input .. dont panic')
            self.submitButton.click()
            
    def submit_exploit_in_phone_field(self):
        for exploit in payloads:
            self.nameField.fill(fd.fname+''+fd.lname)
            self.emailAddressField.fill(fd.email)
            self.phoneNumberField.fill(f"212+{exploit}")
            self.messageField.fill('This is a cool automated test for SQL Injection at phone input .. dont panic')
            self.submitButton.click()
            
    def submit_exploit_in_message_field(self):
        for exploit in payloads:
            self.nameField.fill(fd.fname+''+fd.lname)
            self.emailAddressField.fill(fd.email)
            self.phoneNumberField.fill(fd.tel)
            self.messageField.fill(f"This is a cool automated test for {exploit} .. dont panic")
            self.submitButton.click()
            
    def confirm_form_submission_is_unsuccessful(self, url):
        response = requests.get(url)
        assert response.status_code != 201, f"SQLI InjectionVulnerability occurred using - {0}"
    