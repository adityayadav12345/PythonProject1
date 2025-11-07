import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20
def slow(s=1.0): time.sleep(s)

def test_17_checkboxes_radios():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        slow(1.2)

        # Radios
        radio1 = wait.until(EC.element_to_be_clickable((By.ID, "my-radio-1")))
        radio2 = driver.find_element(By.ID, "my-radio-2")
        radio1.click(); slow(0.6)
        assert radio1.is_selected()
        radio2.click(); slow(0.6)
        assert radio2.is_selected() and not radio1.is_selected()

        # Checkbox
        cb = driver.find_element(By.ID, "my-check-1")
        if not cb.is_selected():
            cb.click(); slow(0.6)
        assert cb.is_selected()
        cb.click(); slow(0.6)
        assert not cb.is_selected()
    finally:
        slow(1)
        driver.quit()
