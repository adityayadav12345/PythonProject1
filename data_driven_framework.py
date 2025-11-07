from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import xml.etree.ElementTree as ET
import time


class DataDrivenFormTest:
    def __init__(self):
        self.driver = None

    def setup_browser(self):
        """Setup Chrome browser"""
        print("\n" + "=" * 50)
        print("SETTING UP BROWSER")
        print("=" * 50)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        time.sleep(2)
        print("Browser opened and website loaded successfully.")

    def read_xml_data(self, file_path="xml_data.xml"):
        """Read XML data from file"""
        print("\n" + "=" * 50)
        print("READING DATA FROM XML FILE")
        print("=" * 50)

        test_cases = []
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            form_section = root.find("FormTests")
            if form_section is not None:
                for test_case in form_section.findall("TestCase"):
                    data = {
                        "TestCaseID": test_case.get("testCaseID"),
                        "Name": test_case.find("Name").text if test_case.find("Name") is not None else "",
                        "Email": test_case.find("Email").text if test_case.find("Email") is not None else "",
                        "Password": test_case.find("Password").text if test_case.find("Password") is not None else "",
                        "ExpectedResult": test_case.find("ExpectedResult").text
                    }
                    test_cases.append(data)

            # Display loaded test data
            for t in test_cases:
                print(f"Loaded Test Case: {t}")

            return test_cases
        except Exception as e:
            print(f"Error reading XML: {e}")
            return []

    def test_form_fields_xml(self):
        """Run form field tests using XML data"""
        print("\n" + "=" * 50)
        print("TESTING FORM FIELDS (XML DATA)")
        print("=" * 50)

        test_cases = self.read_xml_data("xml_data.xml")
        if not test_cases:
            print("No test cases found in XML file.")
            return

        passed = 0
        for case in test_cases:
            name = case["Name"]
            email = case["Email"]
            password = case["Password"]
            expected = case["ExpectedResult"]

            print(f"\n▶ Test Case {case['TestCaseID']}: Expected={expected}")

            try:
                # Locate and clear form fields
                name_field = self.driver.find_element(By.NAME, "name")
                email_field = self.driver.find_element(By.NAME, "email")
                password_field = self.driver.find_element(By.ID, "exampleInputPassword1")

                name_field.clear()
                email_field.clear()
                password_field.clear()

                # Fill the fields
                if name:
                    name_field.send_keys(name)
                if email:
                    email_field.send_keys(email)
                if password:
                    password_field.send_keys(password)

                # Click submit button
                submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
                submit_btn.click()
                time.sleep(1)

                # Determine result
                try:
                    success_msg = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
                    actual_result = "Valid"
                except:
                    actual_result = "Invalid"

                test_passed = actual_result == expected

                if test_passed:
                    print(f"PASS - Actual: {actual_result}")
                    passed += 1
                else:
                    print(f"FAIL - Actual: {actual_result}")

                # Wait a bit between tests
                time.sleep(1)

            except Exception as e:
                print(f"⚠️ Error during test case {case['TestCaseID']}: {e}")

        print(f"\nFinal Results: {passed}/{len(test_cases)} test cases passed.")

    def run_all_tests(self):
        """Run all XML-based form tests"""
        try:
            self.setup_browser()
            self.test_form_fields_xml()

            print("\n" + "=" * 50)
            print("DATA-DRIVEN FORM TESTING COMPLETED")
            print("=" * 50)
        except Exception as e:
            print(f"Error in test execution: {e}")
        finally:
            if self.driver:
                self.driver.quit()
                print("Browser closed.")


if __name__ == "__main__":
    print("🔍 DATA-DRIVEN TEST FRAMEWORK DEMONSTRATION")
    print("Website: https://rahulshettyacademy.com/angularpractice/")
    print("Using XML file for Name, Email, and Password fields.\n")

    demo = DataDrivenFormTest()
    demo.run_all_tests()
