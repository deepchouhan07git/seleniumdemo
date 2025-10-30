import app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[2]")

time.sleep(3)  # just to see the page load

driver.close() #Close single browser window
driver.quit()  #Close multiple browser window
