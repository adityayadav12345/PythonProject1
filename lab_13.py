import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    return driver


class TestEcommerceProducts:

    def test_product_listing_count(self, logged_in_driver):
        driver = logged_in_driver
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Total products: {len(products)}")
        assert len(products) == 6

    def test_add_to_cart_functionality(self, logged_in_driver):
        driver = logged_in_driver
        add_button = driver.find_element(By.CSS_SELECTOR, ".btn_inventory")
        add_button.click()
        time.sleep(0.5)
        assert add_button.text == "Remove"
        print("Product added successfully")

    def test_cart_item_counter(self, logged_in_driver):
        driver = logged_in_driver
        add_buttons = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")
        add_buttons[0].click()
        time.sleep(0.5)

        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"

        add_buttons[1].click()
        time.sleep(0.5)
        assert cart_badge.text == "2"
        print(f"Cart counter: {cart_badge.text}")

    def test_product_price_calculations(self, logged_in_driver):
        driver = logged_in_driver

        first_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item:first-child .inventory_item_price")
        price_value = float(first_price.text.replace("$", ""))
        print(f"Product price: ${price_value}")

        driver.find_element(By.CSS_SELECTOR, ".inventory_item:first-child .btn_inventory").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

        cart_price = driver.find_element(By.CLASS_NAME, "inventory_item_price")
        cart_price_value = float(cart_price.text.replace("$", ""))

        assert cart_price_value == price_value
        print(f"Price verified: ${cart_price_value}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])