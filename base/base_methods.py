from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


class BaseMethods(object):

    def __init__(self, driver, driver_wait=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=driver_wait, poll_frequency=0.1,
                                  ignored_exceptions=[StaleElementReferenceException, NoSuchElementException])

    def wait_until_element_present(self, locator):
        """
        Wait until the element is present
        :param locator: By

        """
        self.wait.until(EC.presence_of_element_located(locator))

    def find_element(self, locator):
        """
        Finds an element by locator and returns WebElement if it exists
        :param locator: By
        :return: WebElement

        """
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(locator)

    def find_elements(self, locator):
        """
        Finds elements by locator and returns list of WebElement if it exists
        :param locator: By
        :return: list of WebElement

        """
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(locator)

    def navigate_to(self, url):
        """
        Navigates to the given url
        :param str url: The url to navigate to

        """
        self.driver.get(url)
        self.wait.until(EC.url_to_be(url))

    def click_element(self, locator):
        """
        Clicks an element by locator
        :param locator: By

        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def scroll_to_element(self, locator, center=False):
        """
        Scrolls to the given location
        :param locator: By
        :param center: Boolean

        """
        self.wait.until(EC.visibility_of_element_located(locator))

        if center:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", locator)
