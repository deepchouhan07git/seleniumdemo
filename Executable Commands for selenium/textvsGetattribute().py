from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://admin-demo.nopcommerce.com/login")

# emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
# emailbox.clear()
# emailbox.send_keys("abc@gmail.com")
#
# print("Result of the text :", emailbox.text) #printed nothing
# print("Result of the GetAttribute('value') :", emailbox.get_attribute('value')) #abc@gmail.com

button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("Result of the text :", button.text)
print("Result of the GetAttribute('value') :", button.get_attribute('value'))
print("Result of the GetAttribute('value') :", button.get_attribute('type'))
