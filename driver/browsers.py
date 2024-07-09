from selenium import webdriver


class Browsers:
    def __init__(self):
        raise NotImplementedError('This class should not be instantiated.')

    @staticmethod
    def get_local_driver(browser):
        if browser.lower() == "chrome":
            return Browsers._get_chrome_driver()
        elif browser.lower() == "firefox":
            return Browsers._get_firefox_driver()
        else:
            return None

    @staticmethod
    def _get_chrome_driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-certificate-errors-spki-list")
        chrome_options.add_argument("--suppress-message-center-popups")
        chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
        chrome_options.add_argument('start-maximized')  # Start browser maximized
        chrome_options.add_argument('disable-infobars')  # Disables the info bar that often shows up in Chrome
        chrome_options.add_argument('--disable-extensions')  # Disable extensions
        chrome_options.accept_insecure_certs = True
        return webdriver.Chrome(options=chrome_options)

    @staticmethod
    def _get_firefox_driver():
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("network.cookie.cookieBehavior", 2)
        return webdriver.Firefox(options=firefox_options)
