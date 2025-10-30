from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

mywait=WebDriverWait(driver,10,ignored_exceptions=[exceptions])

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
searchlink.click()
