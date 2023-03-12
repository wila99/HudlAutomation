from selenium.webdriver.common.by import By

# XPath locator for Hudl Homepage
btnLogin = "//a[@href='/login']"


class PageLoader(object):

    def __init__(self, driver):
        self.driver = driver


class Home_Locator(PageLoader):

    def clickLogin(self):
        return self.driver.find_element(By.XPATH, btnLogin).click()
