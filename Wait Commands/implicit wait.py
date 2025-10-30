from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()


driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

