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

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

alertwnd=driver.switch_to.alert
alertwnd.send_keys("Welcome")
time.sleep(5)
alertwnd.accept() # Close the window by using Ok button
alertwnd.dismiss() # Close the window by using Cancel button
time.sleep(5)

