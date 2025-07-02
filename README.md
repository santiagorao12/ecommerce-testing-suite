# E-Commerce Testing Suite

## Project Overview
Comprehensive testing framework for AutomationExercise.com e-commerce application with focus on critical user journeys and API validation.

## 🎯 What This Project Does
Tests an online shopping website to find bugs and problems. Checks if shopping cart works, user registration functions, checkout process completes successfully, and identifies issues that could block customer purchases.

## 🔧 Technologies Used
- **Automation:** Selenium WebDriver
- **Language:** Python
- **Testing Framework:** pytest
- **Reporting:** HTML reports with screenshots

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
