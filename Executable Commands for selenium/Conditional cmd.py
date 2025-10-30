from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display searchbox =", searchbox.is_displayed())
print("Enable searhbox =", searchbox.is_enabled())

male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(male.is_selected())
print(female.is_selected())

male.click()

print("After selecting radio button :")
print(male.is_selected())
print(female.is_selected())