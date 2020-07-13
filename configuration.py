import pathlib
import logging

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


SAMPLE_FILE_PATH = pathlib.Path(__file__).parent.joinpath("resources", "sample_file.txt").absolute()


class OpenCart:
    ADMIN_USERNAME = "user"
    ADMIN_PASSWORD = "bitnami1"
#


class BitnamiDatabase:
    HOST = "localhost"
    PORT = 3306
    DB_NAME = "bitnami_opencart"
    DB_USER = "bn_opencart"
#


class DriverEventListener(AbstractEventListener):

    def __init__(self, log_filename: str, log_level: int = logging.INFO):
        self.log_filename = log_filename

        self.handler = logging.FileHandler(filename=self.log_filename)
        self.formatter = logging.Formatter(fmt="%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s")
        self.handler.setFormatter(fmt=self.formatter)

        self.logger = logging.getLogger(name=f"{type(self).__name__}")
        self.logger.setLevel(level=log_level)
        self.logger.addHandler(hdlr=self.handler)
    #

    def before_navigate_to(self, url, driver):
        self.logger.info(f"About to navigate to: {url}")
    #

    def after_navigate_to(self, url, driver):
        self.logger.info(f"Navigated to: {url}")
    #

    def before_navigate_back(self, driver):
        self.logger.info("About to navigate back")
    #

    def after_navigate_back(self, driver):
        self.logger.info("Navigated back")
    #

    def before_navigate_forward(self, driver):
        self.logger.info("About to navigate forward")
    #

    def after_navigate_forward(self, driver):
        self.logger.info("Navigated forward")
    #

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for '{value}' by '{by}'")
    #

    def after_find(self, by, value, driver):
        self.logger.info(f"Found '{value}' by '{by}'")
    #

    def before_click(self, element, driver):
        self.logger.info(f"About to click: {element.tag_name}")
    #

    def after_click(self, element, driver):
        self.logger.info(f"Clicked: {element.tag_name}")
    #

    def before_change_value_of(self, element, driver):
        self.logger.info(f"About to change value of: {element.tag_name}")
    #

    def after_change_value_of(self, element, driver):
        self.logger.info(f"Changed value of: {element.tag_name}")
    #

    def before_execute_script(self, script, driver):
        self.logger.info(f"About to execute script: '{script}'")
    #

    def after_execute_script(self, script, driver):
        self.logger.info(f"Executed script: '{script}'")
    #

    def before_close(self, driver):
        self.logger.info(f"About to close {driver}")
    #

    def after_close(self, driver):
        self.logger.info(f"Closed {driver}")
    #

    def before_quit(self, driver):
        self.logger.info(f"About to quit {driver}")
    #

    def after_quit(self, driver):
        self.logger.info(f"Quit from {driver}")
    #

    def on_exception(self, exception, driver):
        self.logger.error(f'Caught {type(exception).__name__}:\n{exception}')
        self.logger.error(f'Saving screenshot to {type(exception).__name__}.png')
        driver.save_screenshot(filename=f'{type(exception).__name__}.png')
    #
#
