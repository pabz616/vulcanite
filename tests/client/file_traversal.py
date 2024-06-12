import pytest
import requests
from playwright.sync_api import Page
# from utils.data import ProjectData as pd
import allure
from allure_commons.types import Severity

Url = input("Please enter the url to test: ")  # pd.target_url
target = "etc/passwd"

ENCODED = {
    # Text encoding
    f"{Url}../../../../../../../{target}"
    # ASCII encoding
    f"{Url}%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f{target}",
    # HEX encoding
    f"{Url}%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/{target}",
    f"{Url}%uff0e%uff0e%u2215{target}",
    # URL encoding
    f"{Url}..%2f..%2f..%2f..%2f..%2f..%2f..%2f{target}",
    # 16 BIT encoding
    f"{Url}..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af{target}",
    f"{Url}%u2215{target}",
    # UTF_8 encoding
    f"{Url}%c0%ae%c0%ae%c0%af{target}",
    # BASE 64
    f"{Url}Li4vLi4vLi4vLi4vLi4v{target}",
    # BINARY encoding
    f"{Url}00101110 00101110 00101111{target}",
    # OCTAL encoding
    f"{Url}56 56 57 56 56 57 56 56 57 56 56 57 56 56 57{target}",
    

}


@pytest.mark.security
@allure.severity(Severity.CRITICAL)
@allure.title("WSTG-ATHZ-01 - Testing Directory Traversal File Include")
@allure.description("Test for path traversal employing a variety of schemes")
@allure.link("https://owasp.org/www-community/attacks/Path_Traversal", name="Test for Path Traversal")    
@pytest.mark.parametrize("target_url", ENCODED)
class TestPathTraversal:
    def test_for_file_traversal_LFI_baseURL(self, page: Page, target_url):
        with allure.step("Visit site and attempt file traversal leading to local file inclusion"):
            page.goto(target_url)
            response = requests.get(target_url)
            assert response.status_code in {400, 404}, f"File traversal occurred at: - {target_url}"