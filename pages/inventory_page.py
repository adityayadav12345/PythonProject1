from selenium.webdriver.common.by import By


class InventoryPage:
    # Locator variables defined at class level
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_page_title(self, driver):
        return driver.find_element(*self.PAGE_TITLE).text

    def get_inventory_count(self, driver):
        return len(driver.find_elements(*self.INVENTORY_ITEMS))

    def logout(self, driver):
        driver.find_element(*self.MENU_BUTTON).click()
        driver.find_element(*self.LOGOUT_LINK).click()

    def get_current_url(self, driver):
        return driver.current_url
