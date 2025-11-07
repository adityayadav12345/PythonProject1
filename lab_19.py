import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20
def slow(s=1.0): time.sleep(s)

def test_19_modal_popup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    try:
        driver.get("https://demoqa.com/modal-dialogs")
        slow(1.2)

        button = wait.until(EC.presence_of_element_located((By.ID, "showSmallModal")))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", button)
        slow(0.8)
        wait.until(EC.element_to_be_clickable((By.ID, "showSmallModal"))).click()
        slow(1.0)

        modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        assert modal.is_displayed()
        slow(0.8)

        close_btn = wait.until(EC.element_to_be_clickable((By.ID, "closeSmallModal")))
        driver.execute_script("arguments[0].click();", close_btn)
        slow(1.0)
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
    finally:
        slow(1)
        driver.quit()
