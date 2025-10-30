from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()
time.sleep(5)