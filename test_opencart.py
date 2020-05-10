def test_main_page(browser):
    footer = browser.find_element_by_tag_name(name="footer")
    assert "OpenCart" in footer.text
#
