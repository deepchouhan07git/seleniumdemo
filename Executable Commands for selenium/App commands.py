from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

time.sleep(20)