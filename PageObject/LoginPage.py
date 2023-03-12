from selenium.webdriver.common.by import By

# Locator for Hudl login page

txtEmailBox = "//input[@id='email']"
txtPasswordBox = "//input[@id='password']"
btnLogin = "//button[@id='logIn']"
btnRememberMe = "//label[@data-qa-id='remember-me-checkbox-label']"
btnIncorrectInput = "/html/body/div/section/div[2]/div/form/div/div[3]/div/p/a"
outErrorDisplay = "//p[@data-qa-id='error-display']"
btnNeedHelp = "//a[@data-qa-id='need-help-link']"

# Locator for Hudl reset password page

txtResetPasswordEmail = "//input[@data-qa-id='password-reset-input']"
btnPasswordReset = "//button[@data-qa-id='password-reset-submit-btn']"
outPasswordRequestError = "//p[@data-qa-id='password-reset-error-display']"


class PageLoader(object):

    def __init__(self, driver):
        self.driver = driver


class Login_Locator(PageLoader):

    def clickLogin(self):
        return self.driver.find_element(By.XPATH, btnLogin).click()

    def inputEmail(self, email):
        return self.driver.find_element(By.XPATH, txtEmailBox).send_keys(email)

    def inputPassword(self, password):
        return self.driver.find_element(By.XPATH, txtPasswordBox).send_keys(password)

    def clickPasswordReset(self):
        return self.driver.find_element(By.XPATH, btnPasswordReset).click()

    def inputResetPassword(self, email):
        return self.driver.find_element(By.XPATH, txtPasswordBox).send_keys(email)

    def errorDisplay(self):
        return self.driver.find_element(By.XPATH, outErrorDisplay).is_displayed()

    def clickHelp(self):
        return self.driver.find_element(By.XPATH, btnNeedHelp).click()

    def inputResetPasswordEmail(self, email):
        return self.driver.find_element(By.XPATH, txtResetPasswordEmail).send_keys(email)
