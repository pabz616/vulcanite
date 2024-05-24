INPUT = '//input[@aria-label="Search"]'
BUTTON = '//button[contains(@class,"nav_search-btn")]'


class TargeInput:
    def __init__(self, page):
        self.page = page
        self.searchField = page.locator(f"xpath={INPUT}")
        self.searchButton = page.locator(f"xpath={BUTTON}")
        self.alert = page.on("dialog", lambda dialog: dialog.accept())

    def submit_exploit(self, payload):
        self.searchButton.click()
        self.searchField.fill(payload)
        self.page.keyboard.press("Enter")
        assert self.alert is None
     
        
        
