#Test Case
#1. Open browser (chrome,ff,edge)
#2. Open URL https://opensource-demo.orangehrmlive.com/
#3. Enter username (Admin)
#4. Enter password (admin123)
#5. Click on Login
# 6. CApture title of the home page
# 7. Verify title of the page : OrangeHRM
# 8. Close browse.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set Chrome options
options = webdriver.ChromeOptions()

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/")

    # Enter credentials
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")

driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")


    # Click login button (use alternative selector)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()







