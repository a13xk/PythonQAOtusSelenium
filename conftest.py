import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption(name="--browser")
    headless = request.config.getoption(name="--headless")

    browser = None

    if browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")

        browser = webdriver.Firefox(options=firefox_options)
    elif browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")

        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True

        browser = webdriver.Chrome(
            options=chrome_options,
            desired_capabilities=capabilities
        )

    yield browser
    browser.quit()
#


@pytest.fixture(scope="function")
def opencart_url(request):
    url = str(request.config.getoption("--opencart_url"))
    if url.startswith("https://localhost"):
        return url
    elif url.startswith("/"):
        return f"https://localhost{url}"
    else:
        raise ValueError(f"Incorrect url: {url}")
#


# Init hook
def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        choices=["firefox", "chrome"],
        help="Web driver for specified browser (defaults to firefox)"
    )

    parser.addoption(
        "--opencart_url",
        action="store",
        default="https://localhost",
        help="OpenCart base URL for tests (defaults to https://localhost)"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode (by default browser starts with GUI)"
    )
#
