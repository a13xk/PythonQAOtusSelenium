import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.support.events import EventFiringWebDriver

from configuration import DriverEventListener

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


def driver_factory(browser_name: str, is_headless: bool = False, webdriver_logging: bool = False) -> webdriver:
    """
    Return webdriver object for a specified browser name
    """
    driver = None

    if browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if is_headless:
            firefox_options.add_argument("--headless")
        if webdriver_logging:
            driver = EventFiringWebDriver(
                driver=webdriver.Firefox(options=firefox_options),
                event_listener=DriverEventListener(log_filename=f"{browser_name}.log")
            )
        else:
            driver = webdriver.Firefox(options=firefox_options)
    elif browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if is_headless:
            chrome_options.add_argument("--headless")
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True

        if webdriver_logging:
            driver = EventFiringWebDriver(
                driver=webdriver.Chrome(
                    options=chrome_options,
                    desired_capabilities=capabilities
                ),
                event_listener=DriverEventListener(log_filename=f"{browser_name}.log")
            )
        else:
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

        if webdriver_logging:
            driver = EventFiringWebDriver(
                driver=webdriver.Opera(
                    options=opera_options,
                    executable_path=OPERA_WEBDRIVER_EXECUTABLE,
                    desired_capabilities=capabilities
                ),
                event_listener=DriverEventListener(log_filename=f"{browser_name}.log")
            )
        else:
            driver = webdriver.Opera(
                options=opera_options,
                executable_path=OPERA_WEBDRIVER_EXECUTABLE,
                desired_capabilities=capabilities
            )
    elif browser_name == "safari":
        # TODO: implement Safari browser
        pass
    else:
        raise NameError("Browser not supported")
    return driver
#


@pytest.fixture(scope="function")
def is_headless(request: FixtureRequest) -> bool:
    """
    Parse "--headless" tag from command line to run browser in headless mode
    """
    if request.config.getoption(name="--headless"):
        return True
    else:
        return False
#


@pytest.fixture(scope="function")
def base_class_logging(request) -> bool:
    """
    Parse "--base_class_logging" tag from command line to log
    actions in base class and its descendants
    """
    if request.config.getoption(name="--base_class_logging"):
        return True
    else:
        return False
#


@pytest.fixture(scope="function")
def webdriver_logging(request) -> bool:
    """
    Parse "--webdriver_logging" tag from command line to run browser
    in event firing webdriver mode (log webdriver actions)
    """
    if request.config.getoption(name="--webdriver_logging"):
        return True
    else:
        return False
#


@pytest.fixture(scope="function")
def browser(request: FixtureRequest, opencart_url: str, is_headless: bool, webdriver_logging: bool) -> webdriver:
    """
    Launch browser and open page specified in --opencart_url command line option
    """
    browser = request.config.getoption(name="--browser")
    driver = driver_factory(
        browser_name=browser,
        is_headless=is_headless,
        webdriver_logging=webdriver_logging
    )
    request.addfinalizer(driver.quit)
    driver.maximize_window()
    driver.get(url=opencart_url)
    return driver
#


@pytest.fixture(scope="function")
def remote_browser(request: FixtureRequest) -> webdriver:
    """
    Launch browser in Selenium Hub specified by 'executor' url
    """
    browser = request.config.getoption(name="--browser")
    executor = request.config.getoption(name="--executor")
    capabilities = {
        "browserName": browser,
        "acceptSslCerts": True,
        "acceptInsecureCerts": True
    }
    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities=capabilities
    )
    request.addfinalizer(driver.quit)
    driver.maximize_window()
    return driver
#


@pytest.fixture(scope="function")
def opencart_url(request: FixtureRequest) -> str:
    """
    URL of OpenCart page (absolute or relative to https://localhost)
    """
    url = str(request.config.getoption("--opencart_url"))
    if url.startswith("https://localhost") or url.startswith("https://demo.opencart.com"):
        return url
    elif url.startswith("/"):
        return f"https://localhost{url}"
    else:
        raise ValueError(f"Incorrect url: {url}")
#


# Init hook
def pytest_addoption(parser: Parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["firefox", "chrome", "opera"],
        help="Web driver for specified browser (defaults to firefox)"
    )

    parser.addoption(
        "--executor",
        action="store",
        default="localhost",
        help="URL of the remote server (defaults to 'http://localhost:4444/wd/hub')"
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

    parser.addoption(
        "--base_class_logging",
        action="store_true",
        help="Log actions in base class and its descendants"
    )

    parser.addoption(
        "--webdriver_logging",
        action="store_true",
        help="Log webdriver actions"
    )
#
