class TestCatalogPage:

    def test_product_category_by_id(self, catalog_page):
        assert catalog_page.find_element(locator=catalog_page.DIV_PRODUCT_CATEGORY)
    #

    def test_img_thumbnail_by_css(self, catalog_page):
        assert catalog_page.find_element(locator=catalog_page.IMG_THUMBNAIL)
    #

    def test_sort_by_label_by_xpath(self, catalog_page):
        assert catalog_page.find_element(locator=catalog_page.LABEL_SORT_BY)
    #

    def test_breadcrumb_by_class_name(self, catalog_page):
        assert catalog_page.find_element(locator=catalog_page.UL_BREADCRUMB)
    #

    def test_product_compare_by_partial_link_text(self, catalog_page):
        assert catalog_page.find_element(locator=catalog_page.A_PRODUCT_COMPARE)
    #
#
