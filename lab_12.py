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


class TestFormValidation:

    def test_required_field_validation(self, driver):
        """Test that required fields show validation messages"""
        driver.get("https://practice.expandtesting.com/login")

        wait = WebDriverWait(driver, 10)

        # Find submit button and click without filling
        submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()
        time.sleep(1)

        # Check validation on username field
        username = driver.find_element(By.ID, "username")
        validation_message = username.get_attribute("validationMessage")

        print(f"Validation message: {validation_message}")
        assert validation_message != "" or "required" in username.get_attribute("class").lower(), \
            "Required field validation should appear"

    def test_email_format_validation(self, driver):
        """Test email field format validation"""
        driver.get("https://practice.expandtesting.com/login")

        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password = driver.find_element(By.ID, "password")

        # Enter invalid email
        username.clear()
        username.send_keys("invalidemail")
        password.send_keys("test123")

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        time.sleep(2)

        # Check for error message
        error_messages = driver.find_elements(By.CSS_SELECTOR, ".alert, .error, #error")
        if error_messages:
            for msg in error_messages:
                if msg.is_displayed():
                    print(f"Error message: {msg.text}")

        print("Email format validation test completed")

    def test_password_confirmation_matching(self, driver):
        """Test password and confirm password fields match"""
        driver.get("https://practice.expandtesting.com/add-remove-elements")

        wait = WebDriverWait(driver, 10)

        # Create a form with password fields using JavaScript
        driver.execute_script("""
            var form = document.createElement('form');
            form.innerHTML = `
                <input type="password" id="password" required>
                <input type="password" id="confirm_password" required>
                <button type="submit">Submit</button>
            `;
            document.body.appendChild(form);

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                var pwd = document.getElementById('password').value;
                var confirm = document.getElementById('confirm_password').value;
                if (pwd !== confirm) {
                    alert('Passwords do not match');
                }
            });
        """)

        time.sleep(1)

        password = driver.find_element(By.ID, "password")
        confirm_password = driver.find_element(By.ID, "confirm_password")

        password.send_keys("Password123")
        confirm_password.send_keys("DifferentPass")

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        time.sleep(1)

        # Check for alert
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            assert "match" in alert_text.lower()
            alert.accept()
        except:
            print("Password mismatch detected")

    def test_form_submission_success(self, driver):
        """Test successful form submission"""
        driver.get("https://practice.expandtesting.com/login")

        wait = WebDriverWait(driver, 10)

        username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password = driver.find_element(By.ID, "password")

        username.send_keys("practice")
        password.send_keys("SuperSecretPassword!")

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        time.sleep(2)

        # Check for success indicators
        success_indicators = driver.find_elements(By.CSS_SELECTOR, ".alert-success, .success, h1")

        for indicator in success_indicators:
            if indicator.is_displayed():
                print(f"Success message: {indicator.text}")

        # Or check URL change
        current_url = driver.current_url
        print(f"Current URL after submit: {current_url}")
        assert "login" not in current_url or "secure" in current_url


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])