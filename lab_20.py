import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 25
def slow(s=1.0): time.sleep(s)

def login_saucedemo(driver, wait):
    driver.get("https://www.saucedemo.com/")
    slow(1.0)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    slow(0.4)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    slow(0.4)
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("/inventory.html"))

def test_20_responsive_design():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    try:
        # Desktop
        driver.set_window_size(1400, 900)
        login_saucedemo(driver, wait)
        slow(0.8)
        grid = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        assert grid.is_displayed()
        slow(0.8)

        # Mobile-ish
        driver.set_window_size(375, 812)
        slow(0.8)

        # Robust open of burger menu
        menu_btn = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        driver.execute_script("arguments[0].click();", menu_btn)  # JS click = more reliable after resize
        slow(0.8)

        # Wait for the slide-out menu to actually open (aria-hidden -> false)
        menu_wrap = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bm-menu-wrap")))
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.CLASS_NAME, "bm-menu-wrap").get_attribute("aria-hidden") == "false"
        )

        # Now the logout link should be visible
        logout_link = wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        assert logout_link.is_displayed()
        slow(0.8)

        # Close the menu cleanly
        cross_btn = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-cross-btn")))
        driver.execute_script("arguments[0].click();", cross_btn)
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.CLASS_NAME, "bm-menu-wrap").get_attribute("aria-hidden") == "true"
        )
        slow(0.6)
    finally:
        slow(1)
        driver.quit()
