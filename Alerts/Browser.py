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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

windID=driver.window_handles
parentid=windID[0]
childid=windID[1]
print(parentid,childid)

# Approach 1
driver.switch_to.window(childid)
print(driver.title)

driver.switch_to.window(parentid)
print(driver.title)
