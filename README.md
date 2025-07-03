# E-Commerce Testing Suite

## Project Overview
Comprehensive testing framework for AutomationExercise.com e-commerce application with focus on critical user journeys and functionality validation.

## 🎯 What This Project Does
Tests an online shopping website to find bugs and problems. Checks if shopping cart works, user registration functions, checkout process completes successfully, and identifies issues that could block customer purchases.

## 🔧 Technologies Used
- **Automation:** Selenium WebDriver
- **Language:** Python
- **Testing Framework:** pytest
- **Browser Support:** Chrome, Firefox, Edge

## 📊 Test Results
- **Total Test Cases:** 32 (18 UI + 14 API)
- **Pass Rate:** 21.9% (7 passed, 25 failed)
- **Critical Bugs Found:** 10+
- **Business Impact:** Revenue-blocking form submission issues identified

## 🐛 Key Findings
### Critical Issues Discovered:
1. **Google Ads Interference:** Form submissions blocked by ad scripts
2. **API Status Code Violations:** Incorrect HTTP responses
3. **Cross-browser Compatibility:** Issues in Safari and Edge
4. **Form Validation:** Missing client-side validation

## 📁 Project Structure
**ecommerce-testing-suite/**
- README.md
- main.py (Main test runner)
- test_advanced_features.py (Advanced e-commerce functionality tests)
- test_api_complete.py (Complete API endpoint validation)
- test_basic_setup.py (Basic setup and configuration tests)
- test_navigation_features.py (Website navigation testing)
- test_shopping_cart.py (Shopping cart functionality tests)
- test_user_management.py (User registration and login tests)
- test_user_management_firefox.py (Firefox-specific user tests)
- test_user_management_fixed.py (Fixed user management issues)
- .idea/ (IDE configuration files)
## 🧪 Test Coverage

### User Management Tests
- User registration and account creation
- Login/logout functionality
- Profile management and updates
- Cross-browser user experience validation

### Shopping Cart Tests
- Add/remove products from cart
- Cart persistence across sessions
- Quantity updates and calculations
- Cart checkout process validation

### Navigation Tests
- Menu functionality and links
- Search feature validation
- Product browsing and filtering
- Page load and responsiveness

### API Tests
- Product data endpoints
- User authentication APIs
- Cart management APIs
- Order processing endpoints

## 🚀 How to Run
```bash
# Run main test suite
python main.py

# Run specific test modules
python test_user_management.py
python test_shopping_cart.py
python test_api_complete.py

# Run browser-specific tests
python test_user_management_firefox.py
