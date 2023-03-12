import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject import LoginPage
from PageObject.HomePage import Home_Locator
from PageObject.LoginPage import Login_Locator
from Config import Config


def loadLogInPage(driver):
    homepage = Home_Locator(driver)
    homepage.clickLogin()


def waitPage(driver, expected_page):
    wait = WebDriverWait(driver, 20).until(EC.url_to_be(expected_page))


class hudlTestCase(unittest.TestCase):

    def setUp(self):
        self.password = Config.password
        self.username = Config.username
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://hudl.com/en_gb')

    def tearDown(self):
        self.driver.close()

    def test_login_page(self):
        # Test opening home page
        loadLogInPage(self.driver)
        self.assertTrue(self.driver.current_url == 'https://www.hudl.com/login')

    def test_sign_in(self):
        # Test successful sign in process
        loadLogInPage(self.driver)
        waitPage(self.driver, 'https://www.hudl.com/login')

        login_page = Login_Locator(self.driver)

        login_page.inputEmail(self.username)
        login_page.inputPassword(self.password)
        login_page.clickLogin()

        waitPage(self.driver, 'https://www.hudl.com/home')
        self.assertTrue(self.driver.current_url == 'https://www.hudl.com/home')

    def test_invalid_sign_in(self):
        # Test unsuccessful sign in process
        loadLogInPage(self.driver)
        waitPage(self.driver, 'https://www.hudl.com/login')

        login_page = Login_Locator(self.driver)

        login_page.inputEmail('test@testing.com')
        login_page.inputPassword('INVALID')
        login_page.clickLogin()

        sleep(2)
        self.assertTrue(self.driver.find_element(By.XPATH, LoginPage.outErrorDisplay).is_displayed())

    def test_reset_password(self):
        loadLogInPage(self.driver)
        waitPage(self.driver, 'https://www.hudl.com/login')
        login_page = Login_Locator(self.driver)

        login_page.clickHelp()
        self.driver.implicitly_wait(3)
        login_page.inputResetPasswordEmail(self.username)
        login_page.clickPasswordReset()

        waitPage(self.driver, 'https://www.hudl.com/login/check-email')

        self.assertTrue(self.driver.current_url == 'https://www.hudl.com/login/check-email')

    def test_reset_password_with_invalid_email(self):
        loadLogInPage(self.driver)
        waitPage(self.driver, 'https://www.hudl.com/login')
        login_page = Login_Locator(self.driver)

        login_page.clickHelp()
        waitPage(self.driver, 'https://www.hudl.com/login/help#')
        sleep(2)
        login_page.inputResetPasswordEmail('testing123@testing.com')
        login_page.clickPasswordReset()

        sleep(2)
        self.assertTrue(self.driver.find_element(By.XPATH, LoginPage.outPasswordRequestError).is_displayed())
