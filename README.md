# vulcanite
Security Automation Framework w. Playwright / Pytest
src. Vulcanite is a rare copper telluride mineral.

# Set Up
1. Confirm that you have the latest version of pythons installed - `python3 --version`
2. Clone the repository
3. Install the latest version of Playwright w. python  - `pip install pytest-playwright`
4. Install allure - `brew install allure` and confirm it was successfully installed - `allure --version`
5. Add Allure Report - `pip install allure-pytest` and import it to your tests, then view with `allure serve allure-results`
6. Install the required browsers - `playwright install`

# Structure
```
..tests
  |_api
    |_test_name.py
  |_client
    |__test_name.py
  |_recon
    |__test_name.py
  |_utils
    |__data.py
  |_reports
    |__report_1.py
```