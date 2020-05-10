import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.opera.options import Options as OperaOptions


OPERA_BROWSER_EXECUTABLE = "/usr/bin/opera"
OPERA_WEBDRIVER_EXECUTABLE = "/usr/local/bin/operadriver"


def driver_factory(browser_name: str, is_headless: bool = False):
    """
    Return webdriver object for a specified browser name
    """
    driver = None

    if browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if is_headless:
            firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    elif browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if is_headless:
            chrome_options.add_argument("--headless")
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        driver = webdriver.Chrome(
            options=chrome_options,
            desired_capabilities=capabilities
        )
    elif browser_name == "yandex":
        # TODO: implement Yandex browser
        pass
    elif browser_name == "opera":
        opera_options = OperaOptions()
        opera_options.binary_location = OPERA_BROWSER_EXECUTABLE
        if is_headless:
            opera_options.add_argument("--headless")

        capabilities = DesiredCapabilities.OPERA.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True

        driver = webdriver.Opera(
            options=opera_options,
            executable_path=OPERA_WEBDRIVER_EXECUTABLE,
            desired_capabilities=capabilities)
    elif browser_name == "safari":
        # TODO: implement Safari browser
        pass
    else:
        raise NameError("Browser not supported")
    return driver
#


@pytest.fixture(scope="function")
def is_headless(request):
    if request.config.getoption(name="--headless"):
        return True
    else:
        return False
#


@pytest.fixture(scope="function")
def browser(request, opencart_url, is_headless):
    browser = request.config.getoption(name="--browser")
    driver = driver_factory(browser_name=browser, is_headless=is_headless)
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=5)
    driver.get(url=opencart_url)
    yield driver
    driver.quit()
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
        choices=["firefox", "chrome", "opera"],
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
