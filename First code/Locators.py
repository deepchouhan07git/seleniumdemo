from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

# ID and NAME Locator
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")


# Link and Partial link text locator
#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()


time.sleep(15)
# driver.quit()
