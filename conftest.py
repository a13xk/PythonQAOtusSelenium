import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration import OpenCartConfiguration
from locators import AdminLoginPage
from locators.administration_page import AdministrationPage

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


@pytest.fixture(scope="function")
def login_to_administration_page(browser):
    wait = WebDriverWait(driver=browser, timeout=15)
    browser.get(url="https://localhost/admin/")
    input_username = browser.find_element_by_id(id_=AdminLoginPage.ID_INPUT_USERNAME)
    input_username.click()
    input_username.send_keys(OpenCartConfiguration.ADMIN_USERNAME)

    input_password = browser.find_element_by_id(id_=AdminLoginPage.ID_INPUT_PASSWORD)
    input_password.click()
    input_password.send_keys(OpenCartConfiguration.ADMIN_PASSWORD)

    login_button = browser.find_element_by_xpath(xpath=AdminLoginPage.XPATH_LOGIN_BUTTON)
    login_button.click()
    wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdministrationPage.XPATH_DASHBOARD_HEADING)))

    yield browser

    logout_button = browser.find_element_by_xpath(xpath=AdministrationPage.XPATH_LOGOUT_BUTTON)
    logout_button.click()

    wait.until(EC.visibility_of_element_located(locator=(By.ID, AdminLoginPage.ID_INPUT_PASSWORD)))


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
        help="URL of OpenCart page (defaults to main page https://localhost)"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode (by default browser starts with GUI)"
    )
#
