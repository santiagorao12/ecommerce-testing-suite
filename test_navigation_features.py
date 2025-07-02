from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class NavigationFeaturesTests:
    def __init__(self):
        service = Service(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "http://automationexercise.com"

    def test_case_6_contact_us_form(self):
        """Test Case 6: Contact Us Form"""
        try:
            print("🧪 Running Test Case 6: Contact Us Form")

            # 1-3. Navigate to home page
            self.driver.get(self.base_url)
            assert "Automation Exercise" in self.driver.title
            print("✓ Home page loaded")

            # 4. Click Contact Us button
            contact_btn = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact us")))
            contact_btn.click()
            print("✓ Clicked Contact Us")

            # 5. Verify 'GET IN TOUCH' is visible
            get_in_touch = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Get In Touch']")))
            assert get_in_touch.is_displayed()
            print("✓ Get In Touch heading visible")

            # 6. Enter name, email, subject and message
            name_field = self.driver.find_element(By.NAME, "name")
            name_field.send_keys("Test User")

            email_field = self.driver.find_element(By.NAME, "email")
            email_field.send_keys("test@example.com")

            subject_field = self.driver.find_element(By.NAME, "subject")
            subject_field.send_keys("Test Subject")

            message_field = self.driver.find_element(By.NAME, "message")
            message_field.send_keys("This is a test message for contact form")
            print("✓ Form fields filled")

            # 8. Click Submit button
            submit_btn = self.driver.find_element(By.NAME, "submit")
            submit_btn.click()

            # 9. Handle OK button (alert)
            time.sleep(2)
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
                print("✓ Alert handled")
            except:
                print("⚠️ No alert found")

            # 10. Verify success message
            time.sleep(2)
            success_msg = self.driver.find_element(By.XPATH,
                                                   "//*[contains(text(),'Success') or contains(text(),'success')]")
            assert success_msg.is_displayed()
            print("✅ Test Case 6: PASSED - Contact form submitted successfully")
            return True

        except Exception as e:
            print(f"❌ Test Case 6: FAILED - {e}")
            return False

    def test_case_7_verify_test_cases_page(self):
        """Test Case 7: Verify Test Cases Page"""
        try:
            print("🧪 Running Test Case 7: Verify Test Cases Page")

            # 1-3. Navigate to home page
            self.driver.get(self.base_url)
            assert "Automation Exercise" in self.driver.title
            print("✓ Home page loaded")

            # 4. Click on Test Cases button
            test_cases_btn = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Test Cases")))
            test_cases_btn.click()
            print("✓ Clicked Test Cases")

            # 5. Verify user is navigated to test cases page successfully
            time.sleep(2)

            # Check URL contains test cases
            current_url = self.driver.current_url
            assert "test_cases" in current_url.lower() or "testcases" in current_url.lower()

            # Check for test cases content
            test_cases_content = self.driver.find_element(By.XPATH,
                                                          "//b[text()='Test Cases'] | //h2[contains(text(),'Test Case')]")
            assert test_cases_content.is_displayed()

            print("✅ Test Case 7: PASSED - Test Cases page loaded successfully")
            return True

        except Exception as e:
            print(f"❌ Test Case 7: FAILED - {e}")
            return False

    def test_case_8_verify_products_page(self):
        """Test Case 8: Verify All Products and product detail page"""
        try:
            print("🧪 Running Test Case 8: Verify All Products and product detail page")

            # 1-3. Navigate to home page
            self.driver.get(self.base_url)
            assert "Automation Exercise" in self.driver.title
            print("✓ Home page loaded")

            # 4. Click on Products button
            products_btn = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Products")))
            products_btn.click()
            print("✓ Clicked Products")

            # 5. Verify user is navigated to ALL PRODUCTS page successfully
            all_products = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//h2[text()='All Products'] | //h2[contains(text(),'Products')]")))
            assert all_products.is_displayed()
            print("✓ All Products page loaded")

            # 6. The products list is visible
            products_list = self.driver.find_elements(By.CLASS_NAME, "product-overlay")
            if not products_list:
                products_list = self.driver.find_elements(By.XPATH, "//div[contains(@class,'product')]")
            assert len(products_list) > 0
            print(f"✓ {len(products_list)} products visible")

            # 7. Click on 'View Product' of first product
            view_product_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//a[contains(@href,'/product_details/') or contains(text(),'View Product')])[1]")))
            view_product_btn.click()
            print("✓ Clicked View Product")

            # 8. User is landed to product detail page
            time.sleep(2)

            # 9. Verify that detail is visible: product name, category, price, availability, condition, brand
            product_info = self.driver.find_element(By.XPATH,
                                                    "//div[@class='product-information'] | //div[contains(@class,'product-detail')]")
            assert product_info.is_displayed()

            # Check for product name (h2 or similar)
            product_name = self.driver.find_element(By.XPATH, "//div[@class='product-information']//h2 | //h1 | //h2")
            assert product_name.is_displayed()

            # Check for price
            price = self.driver.find_element(By.XPATH,
                                             "//*[contains(text(),'Rs.') or contains(text(),'$') or contains(text(),'Price')]")
            assert price.is_displayed()

            print("✅ Test Case 8: PASSED - Products page and product details working")
            return True

        except Exception as e:
            print(f"❌ Test Case 8: FAILED - {e}")
            return False

    def test_case_9_search_product(self):
        """Test Case 9: Search Product"""
        try:
            print("🧪 Running Test Case 9: Search Product")

            # 1-3. Navigate to home page
            self.driver.get(self.base_url)
            assert "Automation Exercise" in self.driver.title
            print("✓ Home page loaded")

            # 4. Click on Products button
            products_btn = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Products")))
            products_btn.click()
            print("✓ Navigated to Products page")

            # 5. Verify user is navigated to ALL PRODUCTS page successfully
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//h2[text()='All Products'] | //h2[contains(text(),'Products')]")))
            print("✓ All Products page confirmed")

            # 6. Enter product name in search input and click search button
            search_input = self.driver.find_element(By.ID, "search_product")
            search_input.clear()
            search_input.send_keys("top")
            print("✓ Entered search term: 'top'")

            search_btn = self.driver.find_element(By.ID, "submit_search")
            search_btn.click()
            print("✓ Clicked search button")

            # 7. Verify 'SEARCHED PRODUCTS' is visible
            time.sleep(2)
            searched_products = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//h2[text()='Searched Products'] | //h2[contains(text(),'Search')]")))
            assert searched_products.is_displayed()
            print("✓ Searched Products heading visible")

            # 8. Verify all the products related to search are visible
            search_results = self.driver.find_elements(By.CLASS_NAME, "product-overlay")
            if not search_results:
                search_results = self.driver.find_elements(By.XPATH, "//div[contains(@class,'product')]")
            assert len(search_results) > 0
            print(f"✓ {len(search_results)} search results found")

            print("✅ Test Case 9: PASSED - Search functionality working")
            return True

        except Exception as e:
            print(f"❌ Test Case 9: FAILED - {e}")
            return False

    def test_case_10_subscription_home(self):
        """Test Case 10: Verify Subscription in home page"""
        try:
            print("🧪 Running Test Case 10: Verify Subscription in home page")

            # 1-3. Navigate to home page
            self.driver.get(self.base_url)
            assert "Automation Exercise" in self.driver.title
            print("✓ Home page loaded")

            # 4. Scroll down to footer
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("✓ Scrolled to footer")

            # 5. Verify text 'SUBSCRIPTION'
            subscription_text = self.driver.find_element(By.XPATH,
                                                         "//h2[text()='Subscription'] | //*[contains(text(),'SUBSCRIPTION')]")
            assert subscription_text.is_displayed()
            print("✓ Subscription text visible")

            # 6. Enter email address in input and click arrow button
            email_input = self.driver.find_element(By.ID, "susbscribe_email")
            email_input.clear()
            email_input.send_keys("test@example.com")
            print("✓ Email entered")

            subscribe_btn = self.driver.find_element(By.ID, "subscribe")
            subscribe_btn.click()
            print("✓ Subscribe button clicked")

            # 7. Verify success message
            time.sleep(3)
            success_msg = self.driver.find_element(By.XPATH,
                                                   "//*[contains(text(),'successfully subscribed') or contains(text(),'Success')]")
            assert success_msg.is_displayed()
            print("✓ Success message displayed")

            print("✅ Test Case 10: PASSED - Subscription functionality working")
            return True

        except Exception as e:
            print(f"❌ Test Case 10: FAILED - {e}")
            return False

    def run_all_navigation_tests(self):
        """Run all navigation and feature tests"""
        results = {}

        results['test_case_6'] = self.test_case_6_contact_us_form()
        results['test_case_7'] = self.test_case_7_verify_test_cases_page()
        results['test_case_8'] = self.test_case_8_verify_products_page()
        results['test_case_9'] = self.test_case_9_search_product()
        results['test_case_10'] = self.test_case_10_subscription_home()

        # Results summary
        passed = sum(results.values())
        total = len(results)
        print(f"\n📊 NAVIGATION & FEATURES TESTS SUMMARY:")
        print(f"✅ Passed: {passed}/{total}")
        print(f"❌ Failed: {total - passed}/{total}")
        print(f"📈 Pass Rate: {(passed / total) * 100:.1f}%")

        self.driver.quit()
        return results


# Run the tests
if __name__ == "__main__":
    test_suite = NavigationFeaturesTests()
    test_suite.run_all_navigation_tests()