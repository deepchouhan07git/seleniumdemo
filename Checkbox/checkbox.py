from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Approach 1
# checkbox=driver.find_element(By.XPATH,"//input[@id='sunday']")
# checkbox.click()

# Approach 2 Print length of the checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# Approach 3 select all the checkboxes
for i in range(len(checkboxes)):
    checkboxes[i].click()

time.sleep(5)

# Approach 4 select last 2
# for i in range(len(checkboxes)-2,7):
#     checkboxes[i].click()

# Approach 5 clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

time.sleep(5)

