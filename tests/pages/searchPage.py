from utils.data import SQLIPayloads as sqli
import requests

INPUT = '//input[@aria-label="Search"]'
BUTTON = '//button[contains(@class,"nav_search-btn")]'

payloads = [
    sqli.sqlInjection,
    sqli.sqlInjection2,
    sqli.sqlInjection3,
    sqli.sqlInjection_encoded,
    sqli.sqlInjection_inline,
    sqli.sqlInjection_lowercase,
    sqli.sqlInjection_nullBytes
]


class SearchInput:
    def __init__(self, page):
        self.page = page
        self.searchField = page.locator(f"xpath={INPUT}")
        self.searchButton = page.locator(f"xpath={BUTTON}")
        self.alert = page.on("dialog", lambda dialog: dialog.accept())
        
    def submit_exploit(self):
        for exploit in payloads:
            self.searchButton.click()
            self.searchField.fill(exploit)
            self.page.keyboard.press("Enter")
            assert self.alert is None, f"SQLI InjectionVulnerability occurred using - {exploit}"
             
    def confirm_search_is_unsuccessful(self, url):
        response = requests.get(url)
        assert response.status_code != 201, f"Redirected occurred with status code {response.status_code}"