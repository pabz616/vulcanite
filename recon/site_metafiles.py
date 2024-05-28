"""
RECON STEP: SCAN FOR META FILES
src: WSTG-INFO-03 - Review Webserver Metafiles for Information Leakage
link: https://owasp.boireau.io:8443/4-web_application_security_testing/01-information_gathering/03-review_webserver_metafiles_for_information_leakage

Test Objectives
1. Identify hidden or obfuscated paths and functionality through the analysis of metadata files.
2. Extract and map other information that could lead to a better understanding of the systems at hand.

"""

import pytest
import webbrowser
from playwright.sync_api import Page
from utils.data import ProjectData as pd
import allure


Url = pd.target_url

METAFILES = {
    f"{Url}robots.txt",
    f"{Url}security.txt",
    f"{Url}humans.txt",
    f"{Url}sitemap.xml"
}


@pytest.mark.security
@pytest.mark.parametrize("target_url", METAFILES)
class TestForMetafiles:
    def test_for_metafiles_in_web_app(self, page: Page, target_url):
        with allure.step("Visit site and check for metafiles"):
            webbrowser.open_new_tab(target_url)
