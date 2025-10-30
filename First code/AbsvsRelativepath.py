from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://www.facebook.com/")
driver.maximize_window()

# Absolute XPATH

# driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").click()

#Relative XPath

# driver.find_element(By.XPATH,"//*[@id='email']").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH,"//*[@id='email']").click()

time.sleep(20)
