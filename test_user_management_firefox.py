from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


class UserManagementTestsFirefox:
    def __init__(self):
        # Use Firefox instead of Edge
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "http://automationexercise.com"
        self.test_email = f"testuser{random.randint(1000, 9999)}@example.com"

    def test_case_1_register_user(self):
        """Test Case 1: Register User - Firefox with Adblocker"""
        try:
            print("🧪 Running Test Case 1: Register User (Firefox)")

            self.driver.get(self.base_url)
            assert "Automation Exercise" in self.driver.title
            print("✓ Home page loaded")

            # Click Signup/Login
            signup_login = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
            signup_login.click()

            # Verify and fill signup form
            signup_text = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))

            name_field = self.driver.find_element(By.NAME, "name")
            name_field.send_keys("Test User")

            email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
            email_field.send_keys(self.test_email)

            signup_button = self.driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
            signup_button.click()

            # Wait for account info page
            account_info = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//b[text()='Enter Account Information']")))

            # Fill account details - should work without ad interference
            title_mr = self.driver.find_element(By.ID, "id_gender1")
            title_mr.click()

            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("TestPassword123")

            # Date of birth
            day_select = Select(self.driver.find_element(By.ID, "days"))
            day_select.select_by_value("15")

            month_select = Select(self.driver.find_element(By.ID, "months"))
            month_select.select_by_value("7")

            year_select = Select(self.driver.find_element(By.ID, "years"))
            year_select.select_by_value("1990")

            # Try to click checkboxes (should work with adblocker)
            try:
                newsletter = self.driver.find_element(By.ID, "newsletter")
                newsletter.click()
                print("✓ Newsletter checkbox clicked")

                offers = self.driver.find_element(By.ID, "optin")
                offers.click()
                print("✓ Offers checkbox clicked")
            except Exception as e:
                print(f"⚠️ Checkbox issue: {e}")

            # Address details
            first_name = self.driver.find_element(By.ID, "first_name")
            first_name.send_keys("Test")

            last_name = self.driver.find_element(By.ID, "last_name")
            last_name.send_keys("User")

            company = self.driver.find_element(By.ID, "company")
            company.send_keys("Test Company")

            address1 = self.driver.find_element(By.ID, "address1")
            address1.send_keys("123 Test Street")

            country = Select(self.driver.find_element(By.ID, "country"))
            country.select_by_value("United States")

            state = self.driver.find_element(By.ID, "state")
            state.send_keys("California")

            city = self.driver.find_element(By.ID, "city")
            city.send_keys("Los Angeles")

            zipcode = self.driver.find_element(By.ID, "zipcode")
            zipcode.send_keys("90210")

            mobile = self.driver.find_element(By.ID, "mobile_number")
            mobile.send_keys("1234567890")

            # Create account - should work without ad blocking
            create_account = self.driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
            create_account.click()

            # Verify account created
            account_created = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']")))
            print("✓ Account created successfully")

            continue_btn = self.driver.find_element(By.XPATH, "//a[@data-qa='continue-button']")
            continue_btn.click()

            # Verify login success
            logged_in = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
            print("✅ Test Case 1: PASSED - User registered successfully")
            return True

        except Exception as e:
            print(f"❌ Test Case 1: FAILED - {e}")
            return False

    # Add the other test methods here (same as before but with Firefox driver)

    def run_firefox_tests(self):
        """Run tests with Firefox"""
        results = {}

        results['test_case_1'] = self.test_case_1_register_user()

        # Results summary
        passed = sum(results.values())
        total = len(results)
        print(f"\n📊 FIREFOX TESTS SUMMARY:")
        print(f"✅ Passed: {passed}/{total}")
        print(f"❌ Failed: {total - passed}/{total}")
        print(f"📈 Pass Rate: {(passed / total) * 100:.1f}%")

        self.driver.quit()
        return results


# Run the tests
if __name__ == "__main__":
    test_suite = UserManagementTestsFirefox()
    test_suite.run_firefox_tests()