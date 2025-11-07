import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20
def slow(s=1.0): time.sleep(s)

def test_15_dynamic_content():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    try:
        driver.get("https://demoqa.com/dynamic-properties")
        slow(1.5)

        # Button becomes clickable ~5s
        wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
        slow(0.5)

        # Color change element: wait up to 20s for 'text-danger' class
        color_el = wait.until(EC.presence_of_element_located((By.ID, "colorChange")))
        WebDriverWait(driver, 20).until(
            lambda d: "text-danger" in d.find_element(By.ID, "colorChange").get_attribute("class")
        )
        assert "text-danger" in color_el.get_attribute("class")
        slow(1)
    finally:
        slow(1)
        driver.quit()
