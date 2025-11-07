import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20

def slow(s=1.2): time.sleep(s)

def test_14_navigation_breadcrumb():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    try:
        # Login
        driver.get("https://www.saucedemo.com/")
        slow(1.5)
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        slow()
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        slow()
        driver.find_element(By.ID, "login-button").click()
        slow(1.5)
        wait.until(EC.url_contains("/inventory.html"))

        # Click the first product (more robust than URL wait)
        first_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item .inventory_item_name")))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", first_link)
        slow(0.5)
        driver.execute_script("arguments[0].click();", first_link)
        slow(1.2)

        # Assert detail page by element, not URL
        details_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name")))
        assert details_name.text.strip() != ""
        slow(1)

        # Back & forward
        driver.back()
        slow(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        driver.forward()
        slow(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name")))
    finally:
        slow(1)
        driver.quit()
