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

#OR XPath

#driver.find_element(By.XPATH,"//*[@id='email' or @name='email']").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH,"//*[@id='email']").click()

#AND Xpath

#driver.find_element(By.XPATH,"//*[@id='email' and @name='email']").send_keys("abc@gmail.com")

# Contains() and start-with()

driver.find_element(By.XPATH,"//input[contains(@id,'email')]").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//input[contains(@name,'pass')]").send_keys("123@123")
driver.find_element(By.XPATH,"//button[starts-with(@name,'login')]").click()



time.sleep(20)
