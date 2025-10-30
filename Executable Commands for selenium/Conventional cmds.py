from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://www.flipkart.com/")
driver.get("https://www.amazon.in/")

driver.back() #Flipkart
driver.forward() #Amazon

driver.refresh()

time.sleep(5)

driver.quit()