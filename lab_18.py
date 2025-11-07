import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20
def slow(s=1.0): time.sleep(s)

def test_18_file_upload(tmp_path):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        slow(1.2)

        file_input = wait.until(EC.presence_of_element_located((By.NAME, "my-file")))
        p = tmp_path / "upload.txt"
        p.write_text("Upload test successful", encoding="utf-8")
        file_input.send_keys(str(p)); slow(0.8)

        driver.find_element(By.TAG_NAME, "form").submit()
        slow(1.0)
        wait.until(EC.visibility_of_element_located((By.ID, "message")))
        assert "received!" in driver.page_source.lower()
    finally:
        slow(1)
        driver.quit()
