from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

# Create ChromeOptions instance
options = webdriver.ChromeOptions()


# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

time.sleep(5)


