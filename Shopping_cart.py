import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def setup_browser():
    """Setup Chrome browser and open eBay homepage."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.ebay.com/")
    yield driver
    driver.quit()


def test_search_laptop(setup_browser):
    """Search for 'laptop' on eBay."""
    driver = setup_browser
    wait = WebDriverWait(driver, 20)

    # Enter 'laptop' in search box
    search_box = wait.until(EC.presence_of_element_located((By.ID, "gh-ac")))
    search_box.clear()
    search_box.send_keys("laptop")

    # Click search button
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gh-search-btn"]/span')))
    search_button.click()
    print("\n✅ Search initiated for 'laptop'")
    time.sleep(5)  # Let the search results load


def open_graphics_processing_dropdown(driver):
    """Opens the 'Graphics Processing Type' dropdown on eBay using aria-expanded attribute."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    wait = WebDriverWait(driver, 20)

    # XPath for the 'Graphics Processing Type' dropdown
    dropdown_xpath = "//h3[contains(., 'Graphics Processing Type')]/div/div"

    try:
        # Wait until the dropdown element is present
        dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))

        # Scroll it into view
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_element)
        time.sleep(2)

        # Click to expand dropdown
        driver.execute_script("arguments[0].click();", dropdown_element)
        print("✅ Opened 'Graphics Processing Type' dropdown successfully.")
    except Exception as e:
        print(f"⚠️ Could not open 'Graphics Processing Type' dropdown: {e}")

    time.sleep(2)




def click_hp_radio_button(driver):

    wait = WebDriverWait(driver, 20)
    hp_radio_xpath = "//*[@id='x-refine__group_1__0']/ul/li[1]/div/a/div/span/input"

    try:
        # Wait until the HP radio button is clickable
        hp_radio = wait.until(EC.element_to_be_clickable((By.XPATH, hp_radio_xpath)))

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", hp_radio)
        time.sleep(2)

        # Click the radio button
        driver.execute_script("arguments[0].click();", hp_radio)
        print("✅ Clicked HP radio button successfully.")
    except Exception as e:
        print(f"⚠️ Could not click HP radio button: {e}")

    # Wait so you can see the HP products load
    time.sleep(3)



def test_apply_hp_filter(setup_browser):
    """Open brand dropdown and select HP filter."""
    driver = setup_browser
    open_graphics_processing_dropdown(driver)
    click_hp_radio_button(driver)
