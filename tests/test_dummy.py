from base.base_test import *
from pages.homepage.insider_homepage import InsiderHomepage


class TestDummy(BaseTest):
    url = "https://useinsider.com/"

    def test_dummy(self):
        """
            Deneme
        """
        self.base_methods.navigate_to(self.url)
        insider_homepage = InsiderHomepage(self.driver)
        insider_homepage.click_company_menu()
        insider_homepage.click_careers_sub_menu()

    def tearDown(self):
        self.quit_driver()
