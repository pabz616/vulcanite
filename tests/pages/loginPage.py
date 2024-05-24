"""
LOCATORS
"""

USN = '//input[@id="form2Example1"]'
PWD = '//input[@id="form2Example2"]'
SUBMIT = '//button[contains(@class,"mb-4")]'
FORGOT_PWD_LINK = '//a[contains(.,"Forgot password?")]'
REMEMBER_ME = '//label[@for="form2Example31"]'


class LoginInput:
    def __init__(self, page):
        self.page = page

# LOGIN FORM
        self.usernameField = page.locator(f"xpath={USN}")
        self.passwordField = page.locator(f"xpath={PWD}")
        self.searchButton = page.locator(f"xpath={SUBMIT}")
    
    # FORGOT PASSWORD
        self.forgotPasswordLink = page.locator(f"xpath={FORGOT_PWD_LINK }")
        
    # REMEMBER ME
        self.rememberMeButton = page.locator(f"xpath={REMEMBER_ME}")
    
    # REGISTER
    
    def submit_exploit(self, payload):
        pass
        assert self.alert is None