# BASELINE TEST TEMPLATE
When writing new tests, employ the following pattern

```
from playwright.sync_api import Page, expect
import allure
from allure_commons.types import Severity
from pathlib import Path


@allure.severity(Severity.CRITICAL)
@allure.parent_suite(parent_suite_name)
@allure.testcase("TMS-1234")
@allure.title("Test scope)"
@allure.description("Reference to source")
@allure.link("https://owasp.boireau.io:8443/4-web_application_security_testing/11-client-side_testing/09-testing_for_clickjacking")
def test_has_title(page: Page):
    with allure.step("Visit site and confirm page title"):
        page.goto("https://playwright.dev/")

        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Playwright"))
        png_bytes = page.screenshot()
        Path("full-page.png").write_bytes(png_bytes)
        allure.attach.file("full-page.png", name="full-page", attachment_type=allure.attachment_type.PNG)
```

Allure documentation - `https://allurereport.org/docs/pytest/`