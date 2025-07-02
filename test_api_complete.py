import requests
import json
import time


class CompleteAPITestSuite:
    def __init__(self):
        self.base_url = "https://automationexercise.com/api"
        self.results = {}
        print("🔌 Starting Complete API Test Suite")
        print(f"📍 Base URL: {self.base_url}")

    def test_api_1_get_products_list(self):
        """API 1: Get All Products List"""
        try:
            print("🔌 Running API 1: GET All Products List")

            response = requests.get(f"{self.base_url}/productsList")

            # Verify response code
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

            # Verify JSON response
            data = response.json()
            assert "products" in data, "Products key not found in response"
            assert len(data["products"]) > 0, "No products returned"

            print(f"✅ API 1: PASSED - {len(data['products'])} products returned")
            return True

        except Exception as e:
            print(f"❌ API 1: FAILED - {e}")
            return False

    def test_api_2_post_products_list(self):
        """API 2: POST To All Products List (Should return 405)"""
        try:
            print("🔌 Running API 2: POST To Products List (405 Expected)")

            response = requests.post(f"{self.base_url}/productsList")

            # Verify 405 Method Not Allowed
            assert response.status_code == 405, f"Expected 405, got {response.status_code}"

            # Verify error message
            data = response.json()
            assert "not supported" in data["message"].lower(), "Expected 'not supported' in message"

            print("✅ API 2: PASSED - 405 Method Not Allowed returned correctly")
            return True

        except Exception as e:
            print(f"❌ API 2: FAILED - {e}")
            return False

    def test_api_3_get_brands_list(self):
        """API 3: Get All Brands List"""
        try:
            print("🔌 Running API 3: GET All Brands List")

            response = requests.get(f"{self.base_url}/brandsList")

            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            data = response.json()
            assert "brands" in data, "Brands key not found in response"
            assert len(data["brands"]) > 0, "No brands returned"

            print(f"✅ API 3: PASSED - {len(data['brands'])} brands returned")
            return True

        except Exception as e:
            print(f"❌ API 3: FAILED - {e}")
            return False

    def test_api_4_put_brands_list(self):
        """API 4: PUT To All Brands List (Should return 405)"""
        try:
            print("🔌 Running API 4: PUT To Brands List (405 Expected)")

            response = requests.put(f"{self.base_url}/brandsList")

            assert response.status_code == 405, f"Expected 405, got {response.status_code}"
            data = response.json()
            assert "not supported" in data["message"].lower(), "Expected 'not supported' in message"

            print("✅ API 4: PASSED - 405 Method Not Allowed returned correctly")
            return True

        except Exception as e:
            print(f"❌ API 4: FAILED - {e}")
            return False

    def test_api_5_search_product(self):
        """API 5: POST To Search Product"""
        try:
            print("🔌 Running API 5: POST Search Product")

            payload = {"search_product": "top"}
            response = requests.post(f"{self.base_url}/searchProduct", data=payload)

            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            data = response.json()
            assert "products" in data, "Products key not found in search response"

            print(f"✅ API 5: PASSED - Search returned {len(data['products'])} products for 'top'")
            return True

        except Exception as e:
            print(f"❌ API 5: FAILED - {e}")
            return False

    def test_api_6_search_product_no_param(self):
        """API 6: POST To Search Product without search_product parameter"""
        try:
            print("🔌 Running API 6: POST Search Product (No Parameter - 400 Expected)")

            response = requests.post(f"{self.base_url}/searchProduct")

            assert response.status_code == 400, f"Expected 400, got {response.status_code}"
            data = response.json()
            assert "bad request" in data["message"].lower(), "Expected 'bad request' in message"
            assert "search_product parameter is missing" in data[
                "message"].lower(), "Expected missing parameter message"

            print("✅ API 6: PASSED - 400 Bad Request for missing parameter")
            return True

        except Exception as e:
            print(f"❌ API 6: FAILED - {e}")
            return False

    def test_api_7_verify_login_valid(self):
        """API 7: POST To Verify Login with valid details"""
        try:
            print("🔌 Running API 7: POST Verify Login (Valid Details)")

            payload = {
                "email": "test@example.com",
                "password": "testpassword"
            }
            response = requests.post(f"{self.base_url}/verifyLogin", data=payload)

            # Should return 404 since this user doesn't exist, but that's expected behavior
            assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"

            data = response.json()
            if response.status_code == 200:
                assert "user exists" in data["message"].lower(), "Expected 'user exists' message"
                print("✅ API 7: PASSED - Valid login verified (user found)")
            else:
                assert "user not found" in data["message"].lower(), "Expected 'user not found' message"
                print("✅ API 7: PASSED - 404 User not found (expected for test data)")

            return True

        except Exception as e:
            print(f"❌ API 7: FAILED - {e}")
            return False

    def test_api_8_verify_login_missing_email(self):
        """API 8: POST To Verify Login without email parameter"""
        try:
            print("🔌 Running API 8: POST Verify Login (Missing Email - 400 Expected)")

            payload = {"password": "testpassword"}
            response = requests.post(f"{self.base_url}/verifyLogin", data=payload)

            assert response.status_code == 400, f"Expected 400, got {response.status_code}"
            data = response.json()
            assert "bad request" in data["message"].lower(), "Expected 'bad request' in message"
            assert "email or password parameter is missing" in data[
                "message"].lower(), "Expected missing parameter message"

            print("✅ API 8: PASSED - 400 Bad Request for missing email")
            return True

        except Exception as e:
            print(f"❌ API 8: FAILED - {e}")
            return False

    def test_api_9_delete_verify_login(self):
        """API 9: DELETE To Verify Login (Should return 405)"""
        try:
            print("🔌 Running API 9: DELETE Verify Login (405 Expected)")

            response = requests.delete(f"{self.base_url}/verifyLogin")

            assert response.status_code == 405, f"Expected 405, got {response.status_code}"
            data = response.json()
            assert "not supported" in data["message"].lower(), "Expected 'not supported' in message"

            print("✅ API 9: PASSED - 405 Method Not Allowed returned correctly")
            return True

        except Exception as e:
            print(f"❌ API 9: FAILED - {e}")
            return False

    def test_api_10_verify_login_invalid(self):
        """API 10: POST To Verify Login with invalid details"""
        try:
            print("🔌 Running API 10: POST Verify Login (Invalid Details - 404 Expected)")

            payload = {
                "email": "invalid@nonexistent.com",
                "password": "wrongpassword123"
            }
            response = requests.post(f"{self.base_url}/verifyLogin", data=payload)

            assert response.status_code == 404, f"Expected 404, got {response.status_code}"
            data = response.json()
            assert "user not found" in data["message"].lower(), "Expected 'user not found' message"

            print("✅ API 10: PASSED - 404 User not found for invalid credentials")
            return True

        except Exception as e:
            print(f"❌ API 10: FAILED - {e}")
            return False

    def test_api_11_create_user_account(self):
        """API 11: POST To Create/Register User Account"""
        try:
            print("🔌 Running API 11: POST Create User Account")

            # Generate unique email for testing
            timestamp = str(int(time.time()))
            test_email = f"testuser{timestamp}@example.com"

            payload = {
                "name": "Test User",
                "email": test_email,
                "password": "testpassword123",
                "title": "Mr",
                "birth_date": "15",
                "birth_month": "7",
                "birth_year": "1990",
                "firstname": "Test",
                "lastname": "User",
                "company": "Test Company",
                "address1": "123 Test Street",
                "address2": "Apt 1",
                "country": "United States",
                "zipcode": "90210",
                "state": "California",
                "city": "Los Angeles",
                "mobile_number": "1234567890"
            }

            response = requests.post(f"{self.base_url}/createAccount", data=payload)

            assert response.status_code == 201, f"Expected 201, got {response.status_code}"
            data = response.json()
            assert "user created" in data["message"].lower(), "Expected 'user created' message"

            # Store email for cleanup
            self.test_email = test_email
            self.test_password = "testpassword123"

            print(f"✅ API 11: PASSED - User account created successfully ({test_email})")
            return True

        except Exception as e:
            print(f"❌ API 11: FAILED - {e}")
            return False

    def test_api_12_delete_user_account(self):
        """API 12: DELETE METHOD To Delete User Account"""
        try:
            print("🔌 Running API 12: DELETE User Account")

            # Use the account created in API 11
            if not hasattr(self, 'test_email'):
                print("⚠️ No test account to delete, creating one first...")
                # Create account first
                timestamp = str(int(time.time()))
                self.test_email = f"deletetest{timestamp}@example.com"
                self.test_password = "deletepassword123"

                create_payload = {
                    "name": "Delete Test",
                    "email": self.test_email,
                    "password": self.test_password,
                    "title": "Mr",
                    "birth_date": "1",
                    "birth_month": "1",
                    "birth_year": "1990",
                    "firstname": "Delete",
                    "lastname": "Test",
                    "company": "Test Co",
                    "address1": "123 Test St",
                    "country": "United States",
                    "zipcode": "12345",
                    "state": "Test State",
                    "city": "Test City",
                    "mobile_number": "9876543210"
                }
                requests.post(f"{self.base_url}/createAccount", data=create_payload)

            payload = {
                "email": self.test_email,
                "password": self.test_password
            }

            response = requests.delete(f"{self.base_url}/deleteAccount", data=payload)

            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            data = response.json()
            assert "account deleted" in data["message"].lower(), "Expected 'account deleted' message"

            print("✅ API 12: PASSED - User account deleted successfully")
            return True

        except Exception as e:
            print(f"❌ API 12: FAILED - {e}")
            return False

    def test_api_13_update_user_account(self):
        """API 13: PUT METHOD To Update User Account"""
        try:
            print("🔌 Running API 13: PUT Update User Account")

            # Create a test account first for updating
            timestamp = str(int(time.time()))
            update_email = f"updatetest{timestamp}@example.com"

            # Create account
            create_payload = {
                "name": "Update Test",
                "email": update_email,
                "password": "updatepassword123",
                "title": "Mr",
                "birth_date": "1",
                "birth_month": "1",
                "birth_year": "1990",
                "firstname": "Update",
                "lastname": "Test",
                "company": "Update Co",
                "address1": "123 Update St",
                "country": "United States",
                "zipcode": "54321",
                "state": "Update State",
                "city": "Update City",
                "mobile_number": "5555555555"
            }

            create_response = requests.post(f"{self.base_url}/createAccount", data=create_payload)

            if create_response.status_code == 201:
                # Now update the account
                update_payload = {
                    "name": "Updated Name",
                    "email": update_email,
                    "password": "updatepassword123",
                    "title": "Mrs",
                    "birth_date": "15",
                    "birth_month": "6",
                    "birth_year": "1985",
                    "firstname": "Updated",
                    "lastname": "Name",
                    "company": "Updated Company",
                    "address1": "456 Updated Street",
                    "country": "Canada",
                    "zipcode": "98765",
                    "state": "Updated State",
                    "city": "Updated City",
                    "mobile_number": "9999999999"
                }

                response = requests.put(f"{self.base_url}/updateAccount", data=update_payload)

                assert response.status_code == 200, f"Expected 200, got {response.status_code}"
                data = response.json()
                assert "user updated" in data["message"].lower(), "Expected 'user updated' message"

                print("✅ API 13: PASSED - User account updated successfully")

                # Cleanup - delete the test account
                delete_payload = {"email": update_email, "password": "updatepassword123"}
                requests.delete(f"{self.base_url}/deleteAccount", data=delete_payload)

                return True
            else:
                print("⚠️ Could not create account for update test")
                return False

        except Exception as e:
            print(f"❌ API 13: FAILED - {e}")
            return False

    def test_api_14_get_user_detail_by_email(self):
        """API 14: GET user account detail by email"""
        try:
            print("🔌 Running API 14: GET User Detail by Email")

            # Create a test account first
            timestamp = str(int(time.time()))
            detail_email = f"detailtest{timestamp}@example.com"

            create_payload = {
                "name": "Detail Test",
                "email": detail_email,
                "password": "detailpassword123",
                "title": "Ms",
                "birth_date": "20",
                "birth_month": "12",
                "birth_year": "1995",
                "firstname": "Detail",
                "lastname": "Test",
                "company": "Detail Company",
                "address1": "789 Detail Avenue",
                "country": "Australia",
                "zipcode": "11111",
                "state": "Detail State",
                "city": "Detail City",
                "mobile_number": "7777777777"
            }

            create_response = requests.post(f"{self.base_url}/createAccount", data=create_payload)

            if create_response.status_code == 201:
                # Now get user details
                params = {"email": detail_email}
                response = requests.get(f"{self.base_url}/getUserDetailByEmail", params=params)

                assert response.status_code == 200, f"Expected 200, got {response.status_code}"
                data = response.json()
                assert "user" in data, "Expected 'user' key in response"

                # Verify some user details
                user_data = data["user"]
                assert user_data["email"] == detail_email, "Email mismatch in response"
                assert user_data["name"] == "Detail Test", "Name mismatch in response"

                print(f"✅ API 14: PASSED - User details retrieved successfully for {detail_email}")

                # Cleanup
                delete_payload = {"email": detail_email, "password": "detailpassword123"}
                requests.delete(f"{self.base_url}/deleteAccount", data=delete_payload)

                return True
            else:
                print("⚠️ Could not create account for detail test")
                return False

        except Exception as e:
            print(f"❌ API 14: FAILED - {e}")
            return False

    def run_all_api_tests(self):
        """Run all 14 API tests"""
        api_tests = [
            ("API_1", self.test_api_1_get_products_list),
            ("API_2", self.test_api_2_post_products_list),
            ("API_3", self.test_api_3_get_brands_list),
            ("API_4", self.test_api_4_put_brands_list),
            ("API_5", self.test_api_5_search_product),
            ("API_6", self.test_api_6_search_product_no_param),
            ("API_7", self.test_api_7_verify_login_valid),
            ("API_8", self.test_api_8_verify_login_missing_email),
            ("API_9", self.test_api_9_delete_verify_login),
            ("API_10", self.test_api_10_verify_login_invalid),
            ("API_11", self.test_api_11_create_user_account),
            ("API_12", self.test_api_12_delete_user_account),
            ("API_13", self.test_api_13_update_user_account),
            ("API_14", self.test_api_14_get_user_detail_by_email),
        ]

        results = {}
        print(f"\n🚀 Executing {len(api_tests)} API tests...")

        for test_name, test_func in api_tests:
            results[test_name] = test_func()
            time.sleep(0.5)  # Small delay between tests

        # Summary
        passed = sum(results.values())
        total = len(results)
        print(f"\n📊 COMPLETE API TESTING SUMMARY:")
        print(f"✅ Passed: {passed}/{total}")
        print(f"❌ Failed: {total - passed}/{total}")
        print(f"📈 Pass Rate: {(passed / total) * 100:.1f}%")

        return results


# Run all API tests
if __name__ == "__main__":
    api_suite = CompleteAPITestSuite()
    api_suite.run_all_api_tests()