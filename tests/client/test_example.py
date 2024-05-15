import re
from playwright.sync_api import Page, expect
import allure
from pathlib import Path


@allure.testcase("TMS-455")
def test_has_title(page: Page):
    with allure.step("Visit site and confirm page title"):
        page.goto("https://playwright.dev/")

        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Playwright"))
        png_bytes = page.screenshot()
        allure.attach(png_bytes, name="full-page", attachment_type=allure.attachment_type.PNG)


@allure.testcase("TMS-456")
def test_get_started_link(page: Page):
    with allure.step("Launch site & click 'Get Started' link"):
        page.goto("https://playwright.dev/")

        # Click the get started link.
        page.get_by_role("link", name="Get started").click()

        # Expects page to have a heading with the name of Installation.
        expect(page.get_by_role("heading", name="Installation")).to_be_visible()
        png_bytes = page.screenshot()
        Path("full-page.png").write_bytes(png_bytes)
        allure.attach.file("full-page.png", name="full-page", attachment_type=allure.attachment_type.PNG)