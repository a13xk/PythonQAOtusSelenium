from locators.catalog_page import CatalogPage


class TestCatalogPage:

    def test_product_category_by_id(self, browser):
        div_product_category = browser.find_element_by_id(id_=CatalogPage.ID_PRODUCT_CATEGORY)
        assert div_product_category
    #

    def test_img_thumbnail_by_css(self, browser):
        img_thumbnail = browser.find_element_by_css_selector(css_selector=CatalogPage.CSS_IMG_THUMBNAIL)
        assert img_thumbnail
    #

    def test_sort_by_label_by_xpath(self, browser):
        label_sort_by = browser.find_element_by_xpath(xpath=CatalogPage.XPATH_SORT_BY_LABEL)
        assert label_sort_by
    #

    def test_breadcrumb_by_class_name(self, browser):
        ul_breadcrumb = browser.find_element_by_class_name(name=CatalogPage.CLASS_BREADCRUMB)
        assert ul_breadcrumb
    #

    def test_product_compare_by_partial_link_text(self, browser):
        a_product_compare = browser.find_element_by_partial_link_text(link_text=CatalogPage.PARTIAL_LINK_TEXT_PRODUCT_COMPARE)
        assert a_product_compare
    #
#
