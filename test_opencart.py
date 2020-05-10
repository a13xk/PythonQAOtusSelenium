def test_main_page(browser, opencart_url):
    browser.get(opencart_url)
    footer = browser.find_element_by_tag_name(name="footer")
    assert "OpenCart" in footer.text
#
