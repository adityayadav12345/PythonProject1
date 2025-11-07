"""
Test 11: Login Page Automation
Tests login functionality on https://www.saucedemo.com/
Run with: pytest test_11_login_automation.py -v
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestLogin:
    @pytest.fixture
    def driver(self):
        """Setup and teardown for Chrome driver"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        """Test successful login with valid credentials"""
        driver.get("https://www.saucedemo.com/")

        # Enter valid credentials
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Verify successful login by checking URL
        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory.html")
        )

        assert "inventory.html" in driver.current_url
        assert driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()

    def test_login_with_invalid_username(self, driver):
        """Test login failure with invalid username"""
        driver.get("https://www.saucedemo.com/")

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("invalid_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Verify error message appears
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )

        assert error_message.is_displayed()
        assert "Epic sadface" in error_message.text

    def test_login_with_invalid_password(self, driver):
        """Test login failure with invalid password"""
        driver.get("https://www.saucedemo.com/")

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("wrong_password")
        login_button.click()

        # Check error message
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error_message.is_displayed()
        assert "Username and password do not match" in error_message.text

    def test_login_with_empty_credentials(self, driver):
        """Test login with empty username and password"""
        driver.get("https://www.saucedemo.com/")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Verify error for required username
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error_message.is_displayed()
        assert "Username is required" in error_message.text

    def test_page_redirection_after_login(self, driver):
        """Verify page redirects to inventory after successful login"""
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Wait for redirection
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

        # Verify page title
        assert "Swag Labs" in driver.title


if __name__ == "__main__":
    pytest.main([__file__, "-v"])