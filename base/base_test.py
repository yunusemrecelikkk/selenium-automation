import unittest

from base.base_methods import BaseMethods
from driver.driver_manager import DriverManager
from driver.browsers import Browsers


class BaseTest(unittest.TestCase):

    driver = None
    base_methods = None
    # TODO: Create settings env file and read browser key from the file or read the key from args
    driver_wait = 30
    # TODO: Create settings env file and read browser key from the file or read the key from args
    page_load_timeout = 120

    def setUp(self):
        # TODO: Create settings env file and read browser key from the file or read the key from args
        self.browser = 'chrome'

        DriverManager.set_driver(Browsers.get_local_driver(self.browser))
        self.driver = DriverManager.get_driver()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(self.driver_wait)
        self.driver.set_page_load_timeout(self.page_load_timeout)
        self.base_methods = BaseMethods(self.driver, self.driver_wait)

    def quit_driver(self):
        self.driver.quit()
