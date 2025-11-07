from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import openpyxl
import csv
import xml.etree.ElementTree as ET
import time
import os
class DataDrivenDemo:
    def __init__(self):
        self.driver = None

    def setup_browser(self):
        """Setup Chrome browser"""
        self.driver = webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        time.sleep(2)
        print("Browser opened and website loaded")

    def read_excel_data(self):
        """Read test data from Excel file"""
        print("\n" + "=" * 50)
        print("READING DATA FROM EXCEL FILE")
        print("=" * 50)

        test_cases = []
        try:
            workbook = openpyxl.load_workbook('excel_data.xlsx')
            sheet = workbook["NameTests"]

            headers = [cell.value for cell in sheet[1]]

            for row in sheet.iter_rows(min_row=2, values_only=True):
                if row[0]:
                    test_case = dict(zip(headers, row))
                    test_cases.append(test_case)

            workbook.close()

            # Display the data
            for test_case in test_cases:
                print(f"Test Case: {test_case}")

            return test_cases

        except Exception as e:
            print(f"Error reading Excel: {e}")
            return []

    def read_csv_data(self):
        """Read test data from CSV file"""
        print("\n" + "=" * 50)
        print("READING DATA FROM CSV FILE")
        print("=" * 50)

        test_cases = []
        try:
            with open('test_data/csv_data.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    test_cases.append(row)

            # Display the data
            for test_case in test_cases:
                print(f"Test Case: {test_case}")

            return test_cases

        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []

    def read_xml_data(self):
        """Read test data from XML file"""
        print("\n" + "=" * 50)
        print("READING DATA FROM XML FILE")
        print("=" * 50)

        test_cases = []
        try:
            tree = ET.parse('test_data/xml_data.xml')
            root = tree.getroot()

            phone_section = root.find("PhoneTests")

            if phone_section is not None:
                for test_case in phone_section.findall('TestCase'):
                    test_data = {
                        'TestCaseID': test_case.get('testCaseID'),
                        'Phone': test_case.find('Phone').text,
                        'ExpectedResult': test_case.find('ExpectedResult').text
                    }
                    test_cases.append(test_data)

            # Display the data
            for test_case in test_cases:
                print(f"Test Case: {test_case}")

            return test_cases

        except Exception as e:
            print(f"Error reading XML: {e}")
            return []

    def test_name_field_excel(self):
        """Test name field using Excel data"""
        print("\n" + "=" * 50)
        print("TESTING NAME FIELD (EXCEL DATA)")
        print("=" * 50)

        test_cases = self.read_excel_data()

        if not test_cases:
            print("No test cases found in Excel")
            return

        passed = 0
        for test_case in test_cases:
            name = test_case['Name']
            expected = test_case['ExpectedResult']

            print(f"\nTesting: Name='{name}', Expected={expected}")

            try:
                # Find and test name field
                name_field = self.driver.find_element(By.ID, "name")
                name_field.clear()

                if name:
                    name_field.send_keys(name)

                # Click submit
                submit_btn = self.driver.find_element(By.XPATH, "//button[text()='Submit']")
                submit_btn.click()
                time.sleep(1)

                # Check result
                field_class = name_field.get_attribute("class")
                has_error = "error" in field_class
                actual_result = "Invalid" if has_error else "Valid"

                test_passed = actual_result == expected

                if test_passed:
                    print(f"✓ PASS - Actual: {actual_result}")
                    passed += 1
                else:
                    print(f"✗ FAIL - Actual: {actual_result}")

            except Exception as e:
                print(f"Error during test: {e}")

        print(f"\nName Field Results: {passed}/{len(test_cases)} passed")

    def test_email_field_csv(self):
        """Test email field using CSV data"""
        print("\n" + "=" * 50)
        print("TESTING EMAIL FIELD (CSV DATA)")
        print("=" * 50)

        test_cases = self.read_csv_data()

        if not test_cases:
            print("No test cases found in CSV")
            return

        passed = 0
        for test_case in test_cases:
            email = test_case['Email']
            expected = test_case['ExpectedResult']

            print(f"\nTesting: Email='{email}', Expected={expected}")

            try:
                # Find and test email field
                email_field = self.driver.find_element(By.ID, "email")
                email_field.clear()

                if email:
                    email_field.send_keys(email)

                # Click submit
                submit_btn = self.driver.find_element(By.XPATH, "//button[text()='Submit']")
                submit_btn.click()
                time.sleep(1)

                # Check result
                field_class = email_field.get_attribute("class")
                has_error = "error" in field_class
                actual_result = "Invalid" if has_error else "Valid"

                test_passed = actual_result == expected

                if test_passed:
                    print(f"✓ PASS - Actual: {actual_result}")
                    passed += 1
                else:
                    print(f"✗ FAIL - Actual: {actual_result}")

            except Exception as e:
                print(f"Error during test: {e}")

        print(f"\nEmail Field Results: {passed}/{len(test_cases)} passed")

    def test_phone_field_xml(self):
        """Test phone field using XML data"""
        print("\n" + "=" * 50)
        print("TESTING PHONE FIELD (XML DATA)")
        print("=" * 50)

        test_cases = self.read_xml_data()

        if not test_cases:
            print("No test cases found in XML")
            return

        passed = 0
        for test_case in test_cases:
            phone = test_case['Phone']
            expected = test_case['ExpectedResult']

            print(f"\nTesting: Phone='{phone}', Expected={expected}")

            try:
                # Find and test phone field
                phone_field = self.driver.find_element(By.ID, "phone")
                phone_field.clear()

                if phone:
                    phone_field.send_keys(phone)

                # Click submit
                submit_btn = self.driver.find_element(By.XPATH, "//button[text()='Submit']")
                submit_btn.click()
                time.sleep(1)

                # Check result
                field_class = phone_field.get_attribute("class")
                has_error = "error" in field_class
                actual_result = "Invalid" if has_error else "Valid"

                test_passed = actual_result == expected

                if test_passed:
                    print(f"✓ PASS - Actual: {actual_result}")
                    passed += 1
                else:
                    print(f"✗ FAIL - Actual: {actual_result}")

            except Exception as e:
                print(f"Error during test: {e}")

        print(f"\nPhone Field Results: {passed}/{len(test_cases)} passed")

    def run_all_tests(self):
        """Run all data-driven tests"""
        try:
            self.setup_browser()

            # Test with different data sources
            self.test_name_field_excel()  # Uses Excel data
            self.test_email_field_csv()  # Uses CSV data
            self.test_phone_field_xml()  # Uses XML data

            print("\n" + "=" * 50)
            print("DATA-DRIVEN FRAMEWORK DEMO COMPLETED")
            print("=" * 50)
            print("✓ Excel file used for Name field tests")
            print("✓ CSV file used for Email field tests")
            print("✓ XML file used for Phone field tests")
            print("\nEach function uses different data source!")

        except Exception as e:
            print(f"Error in test execution: {e}")
        finally:
            if self.driver:
                self.driver.quit()
                print("\nBrowser closed")


if __name__ == "__main__":
    print("DATA-DRIVEN FRAMEWORK DEMONSTRATION")
    print("Website: https://testautomationpractice.blogspot.com/")
    print("\nThis demo shows 3 functions using different data sources:")
    print("1. Excel file for Name field")
    print("2. CSV file for Email field")
    print("3. XML file for Phone field")
    print()

    demo = DataDrivenDemo()
    demo.run_all_tests()