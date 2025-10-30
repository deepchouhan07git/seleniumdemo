from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://facebook.com")
driver.maximize_window()

#CSS Selector
# tag and id combination
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")

# tag and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")

time.sleep(20)
