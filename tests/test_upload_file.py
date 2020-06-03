def test_upload_file(mozilla_input_page, sample_file_path):
    input_id_file = mozilla_input_page.find_element(locator=mozilla_input_page.INPUT_ID_FILE)
    input_id_file.send_keys(sample_file_path)
    mozilla_input_page.find_element(locator=mozilla_input_page.BUTTON_SUBMIT).click()
#
