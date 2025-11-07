import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20
def slow(s=1.0): time.sleep(s)

def test_16_dropdown_select():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        slow(1.2)

        dropdown = Select(wait.until(EC.visibility_of_element_located((By.NAME, "my-select"))))
        assert dropdown.first_selected_option is not None
        slow(0.8)

        dropdown.select_by_visible_text("Two")
        slow(0.8)
        assert dropdown.first_selected_option.text == "Two"
    finally:
        slow(1)
        driver.quit()
