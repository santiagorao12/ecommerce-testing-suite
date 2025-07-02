from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time


def test_homepage_loads():
    # Use Edge WebDriver
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)

    try:
        driver.get("https://automationexercise.com")
        assert "Automation Exercise" in driver.title
        print("✓ Homepage loads successfully")

        login_link = driver.find_element(By.LINK_TEXT, "Signup / Login")
        login_link.click()
        time.sleep(2)

        assert "Login" in driver.page_source
        print("✓ Navigation to login works")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_homepage_loads()