from selenium.webdriver.common.by import By


class LoginPage:
    # Locator variables defined at class level
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def open(self, driver):
        driver.get("https://www.saucedemo.com/")

    def enter_username(self, driver, username):
        driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, driver, password):
        driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self, driver):
        driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, driver, username, password):
        self.enter_username(driver, username)
        self.enter_password(driver, password)
        self.click_login(driver)

    def get_error_message(self, driver):
        return driver.find_element(*self.ERROR_MESSAGE).text
