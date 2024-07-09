from selenium.webdriver.common.by import By

from base.base_methods import BaseMethods


class InsiderHomepage:
    """Insider homepage https://useinsider.com/ """

    LOGO = (By.CSS_SELECTOR, "nav#navigation > div.container-fluid > a > img")
    COMPANY_MENU = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(),'Company')]")
    CAREERS_SUB_MENU = (By.CSS_SELECTOR, "a[href='https://useinsider.com/careers/']")

    def __init__(self, driver):
        self.driver = driver
        self.base_methods = BaseMethods(driver)
        self.check()

    def check(self):
        self.base_methods.wait_until_element_present(self.LOGO)

    def click_company_menu(self):
        """
        Clicks the company menu

        """
        self.base_methods.click_element(self.COMPANY_MENU)

    def click_careers_sub_menu(self):
        """
        Clicks the careers sub-menu

        """
        self.base_methods.click_element(self.CAREERS_SUB_MENU)
