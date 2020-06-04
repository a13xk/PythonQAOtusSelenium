import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.opera.options import Options as OperaOptions

pytest_plugins = [
    "fixtures.fixtures_admin_login_page",
    "fixtures.fixtures_administration_page",
    "fixtures.fixtures_catalog_page",
    "fixtures.fixtures_login_page",
    "fixtures.fixtures_main_page",
    "fixtures.fixtures_product_page",
    "fixtures.fixtures_mozilla_input_page"
]

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
    """
    Parse "--headless" tag from command line to run browser in headless mode
    """
    if request.config.getoption(name="--headless"):
        return True
    else:
        return False
#


@pytest.fixture(scope="function")
def browser(request, opencart_url, is_headless):
    """
    Launch browser and open page specified in --opencart_url command line option
    """
    browser = request.config.getoption(name="--browser")
    driver = driver_factory(browser_name=browser, is_headless=is_headless)
    driver.maximize_window()
    # driver.implicitly_wait(time_to_wait=5)
    driver.get(url=opencart_url)
    yield driver
    driver.quit()
#


@pytest.fixture(scope="function")
def opencart_url(request):
    """
    URL of OpenCart page (absolute or relative to https://localhost)
    """
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
        default="chrome",
        choices=["firefox", "chrome", "opera"],
        help="Web driver for specified browser (defaults to firefox)"
    )

    parser.addoption(
        "--opencart_url",
        action="store",
        default="https://localhost",
        help="URL of OpenCart page (defaults to main page https://localhost)"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode (by default browser starts with GUI)"
    )
#
