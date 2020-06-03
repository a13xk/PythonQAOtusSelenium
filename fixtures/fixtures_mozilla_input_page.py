import pytest

from configuration import SAMPLE_FILE_PATH
from pages.mozilla_input_page import MozillaInputPage


@pytest.fixture(scope="function")
def mozilla_input_page(browser) -> MozillaInputPage:
    mozilla_input_page = MozillaInputPage(driver=browser)
    mozilla_input_page.open_page()
    frame = mozilla_input_page.find_element(locator=mozilla_input_page.FRAME_BASIC_EXAMPLE)
    browser.execute_script("arguments[0].scrollIntoView();", frame)
    browser.switch_to.frame(frame_reference=frame)
    return mozilla_input_page
#


@pytest.fixture(scope="function")
def sample_file_path() -> str:
    if SAMPLE_FILE_PATH.is_file():
        return str(SAMPLE_FILE_PATH)
    else:
        raise FileNotFoundError(f"No file found at path {SAMPLE_FILE_PATH}")
#
