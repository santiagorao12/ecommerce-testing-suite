from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random


class UserManagementTests:
    def __init__(self):
        service = Service(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.base_url = "http://automationexercise.com"
        self.test_email = f"testuser{random.randint(1000, 9999)}@example.com"

    def test_case_1_register_user(self):
        """Test Case 1: Register User"""
        try:
            print("🧪 Running Test Case 1: Register User")

            # 1-3. Launch browser and verify home page
            self.driver.get(self.base_url)
            assert "Automation Exercise" in self.driver.title
            print("✓ Home page loaded")

            # 4. Click Signup/Login
            signup_login = self.driver.find_element(By.LINK_TEXT, "Signup / Login")
            signup_login.click()

            # 5. Verify 'New User Signup!' is visible
            signup_text = self.driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
            assert signup_text.is_displayed()
            print("✓ Signup form visible")

            # 6-7. Enter name and email, click Signup
            name_field = self.driver.find_element(By.NAME, "name")
            name_field.send_keys("Test User")

            email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
            email_field.send_keys(self.test_email)

            signup_button = self.driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
            signup_button.click()
            time.sleep(2)

            # 8. Verify 'ENTER ACCOUNT INFORMATION' is visible
            account_info = self.driver.find_element(By.XPATH, "//b[text()='Enter Account Information']")
            assert account_info.is_displayed()

            # 9. Fill account details
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

            # 10-11. Select checkboxes
            newsletter = self.driver.find_element(By.ID, "newsletter")
            newsletter.click()

            offers = self.driver.find_element(By.ID, "optin")
            offers.click()

            # 12. Fill address details
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

            # 13. Click Create Account
            create_account = self.driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
            create_account.click()
            time.sleep(3)

            # 14. Verify 'ACCOUNT CREATED!'
            account_created = self.driver.find_element(By.XPATH, "//b[text()='Account Created!']")
            assert account_created.is_displayed()
            print("✓ Account created successfully")

            # 15. Click Continue
            continue_btn = self.driver.find_element(By.XPATH, "//a[@data-qa='continue-button']")
            continue_btn.click()
            time.sleep(2)

            # 16. Verify 'Logged in as username'
            logged_in = self.driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]")
            assert logged_in.is_displayed()
            print("✅ Test Case 1: PASSED - User registered successfully")

            return True

        except Exception as e:
            print(f"❌ Test Case 1: FAILED - {e}")
            return False

    def test_case_2_login_correct_credentials(self):
        """Test Case 2: Login User with correct email and password"""
        try:
            print("🧪 Running Test Case 2: Login with correct credentials")

            # 1-3. Navigate to home page
            self.driver.get(self.base_url)

            # 4. Click Signup/Login
            signup_login = self.driver.find_element(By.LINK_TEXT, "Signup / Login")
            signup_login.click()

            # 5. Verify 'Login to your account' is visible
            login_text = self.driver.find_element(By.XPATH, "//h2[text()='Login to your account']")
            assert login_text.is_displayed()

            # 6. Enter correct email and password
            email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
            email_field.send_keys(self.test_email)

            password_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
            password_field.send_keys("TestPassword123")

            # 7. Click login button
            login_btn = self.driver.find_element(By.XPATH, "//button[@data-qa='login-button']")
            login_btn.click()
            time.sleep(2)

            # 8. Verify 'Logged in as username'
            logged_in = self.driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]")
            assert logged_in.is_displayed()
            print("✅ Test Case 2: PASSED - Login successful")

            return True

        except Exception as e:
            print(f"❌ Test Case 2: FAILED - {e}")
            return False

    def test_case_3_login_incorrect_credentials(self):
        """Test Case 3: Login User with incorrect email and password"""
        try:
            print("🧪 Running Test Case 3: Login with incorrect credentials")

            # Navigate to login page
            self.driver.get(self.base_url)
            signup_login = self.driver.find_element(By.LINK_TEXT, "Signup / Login")
            signup_login.click()

            # Enter incorrect credentials
            email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
            email_field.clear()
            email_field.send_keys("wrong@email.com")

            password_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
            password_field.clear()
            password_field.send_keys("wrongpassword")

            # Click login
            login_btn = self.driver.find_element(By.XPATH, "//button[@data-qa='login-button']")
            login_btn.click()
            time.sleep(2)

            # Verify error message
            error_msg = self.driver.find_element(By.XPATH, "//p[text()='Your email or password is incorrect!']")
            assert error_msg.is_displayed()
            print("✅ Test Case 3: PASSED - Error message displayed correctly")

            return True

        except Exception as e:
            print(f"❌ Test Case 3: FAILED - {e}")
            return False

    def test_case_4_logout_user(self):
        """Test Case 4: Logout User"""
        try:
            print("🧪 Running Test Case 4: Logout User")

            # First login (reuse login flow)
            self.driver.get(self.base_url)
            signup_login = self.driver.find_element(By.LINK_TEXT, "Signup / Login")
            signup_login.click()

            email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
            email_field.send_keys(self.test_email)

            password_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
            password_field.send_keys("TestPassword123")

            login_btn = self.driver.find_element(By.XPATH, "//button[@data-qa='login-button']")
            login_btn.click()
            time.sleep(2)

            # 9. Click Logout
            logout_btn = self.driver.find_element(By.LINK_TEXT, "Logout")
            logout_btn.click()
            time.sleep(2)

            # 10. Verify user is navigated to login page
            login_text = self.driver.find_element(By.XPATH, "//h2[text()='Login to your account']")
            assert login_text.is_displayed()
            print("✅ Test Case 4: PASSED - Logout successful")

            return True

        except Exception as e:
            print(f"❌ Test Case 4: FAILED - {e}")
            return False

    def test_case_5_register_existing_email(self):
        """Test Case 5: Register User with existing email"""
        try:
            print("🧪 Running Test Case 5: Register with existing email")

            # Navigate to signup
            self.driver.get(self.base_url)
            signup_login = self.driver.find_element(By.LINK_TEXT, "Signup / Login")
            signup_login.click()

            # Try to register with existing email
            name_field = self.driver.find_element(By.NAME, "name")
            name_field.send_keys("Another User")

            email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
            email_field.send_keys(self.test_email)  # Use same email as before

            signup_button = self.driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
            signup_button.click()
            time.sleep(2)

            # Verify error message
            error_msg = self.driver.find_element(By.XPATH, "//p[text()='Email Address already exist!']")
            assert error_msg.is_displayed()
            print("✅ Test Case 5: PASSED - Duplicate email error displayed")

            return True

        except Exception as e:
            print(f"❌ Test Case 5: FAILED - {e}")
            return False

    def cleanup_delete_account(self):
        """Delete the test account"""
        try:
            # Login first
            self.driver.get(self.base_url)
            signup_login = self.driver.find_element(By.LINK_TEXT, "Signup / Login")
            signup_login.click()

            email_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
            email_field.send_keys(self.test_email)

            password_field = self.driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
            password_field.send_keys("TestPassword123")

            login_btn = self.driver.find_element(By.XPATH, "//button[@data-qa='login-button']")
            login_btn.click()
            time.sleep(2)

            # Delete account
            delete_btn = self.driver.find_element(By.LINK_TEXT, "Delete Account")
            delete_btn.click()
            time.sleep(2)

            account_deleted = self.driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
            assert account_deleted.is_displayed()
            print("🗑️ Test account cleaned up successfully")

        except Exception as e:
            print(f"⚠️ Cleanup failed: {e}")

    def run_all_user_tests(self):
        """Run all user management tests"""
        results = {}

        # Run tests in sequence
        results['test_case_1'] = self.test_case_1_register_user()
        results['test_case_2'] = self.test_case_2_login_correct_credentials()
        results['test_case_3'] = self.test_case_3_login_incorrect_credentials()
        results['test_case_4'] = self.test_case_4_logout_user()
        results['test_case_5'] = self.test_case_5_register_existing_email()

        # Cleanup
        self.cleanup_delete_account()

        # Results summary
        passed = sum(results.values())
        total = len(results)
        print(f"\n📊 USER MANAGEMENT TESTS SUMMARY:")
        print(f"✅ Passed: {passed}/{total}")
        print(f"❌ Failed: {total - passed}/{total}")
        print(f"📈 Pass Rate: {(passed / total) * 100:.1f}%")

        self.driver.quit()
        return results


# Run the tests
if __name__ == "__main__":
    test_suite = UserManagementTests()
    test_suite.run_all_user_tests()