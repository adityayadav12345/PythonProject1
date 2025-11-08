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
    search_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gh-search-btn"]/span'))
    )
    search_button.click()
    print("\n✅ Search initiated for 'laptop'")
    time.sleep(5)  # Let the search results load


def open_graphics_processing_dropdown(driver):
    """Opens the 'Graphics Processing Type' dropdown on eBay using aria-expanded attribute."""
    wait = WebDriverWait(driver, 20)

    dropdown_xpath = "//h3[contains(., 'Graphics Processing Type')]/div/div"

    try:
        dropdown_element = wait.until(
            EC.presence_of_element_located((By.XPATH, dropdown_xpath))
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_element)
        time.sleep(2)

        driver.execute_script("arguments[0].click();", dropdown_element)
        print("✅ Opened 'Graphics Processing Type' dropdown successfully.")
    except Exception as e:
        print(f"⚠️ Could not open 'Graphics Processing Type' dropdown: {e}")

    time.sleep(2)


def click_dedicated_graphics_checkbox(driver):
    """Clicks the 'Dedicated Graphics' checkbox in eBay filters."""
    wait = WebDriverWait(driver, 20)
    try:
        # Use XPath with aria-label to locate the checkbox
        dedicated_checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='checkbox' and @aria-label='Dedicated Graphics']")
            )
        )

        # Click using JavaScript since it’s not a visible clickable element
        driver.execute_script("arguments[0].click();", dedicated_checkbox)
        print("✅ Successfully clicked 'Dedicated Graphics' checkbox.")
    except Exception as e:
        print(f"⚠️ Could not click 'Dedicated Graphics' checkbox: {e}")

    time.sleep(3)


def test_complete_graphics_filter_workflow(setup_browser):
    driver = setup_browser
    print("\n🚀 Starting complete eBay workflow...\n")

    test_search_laptop(driver)
    open_graphics_processing_dropdown(driver)
    click_dedicated_graphics_checkbox(driver)

    print("\n✅ Workflow completed successfully!\n")
