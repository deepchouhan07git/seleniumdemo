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

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Login']").click()

myalert=driver.switch_to.alert
time.sleep(5)
myalert.accept()



