# XPATHaxes

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
driver.maximize_window()

#Self
txt_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Lupin Ltd.')]/self::a").text
print(txt_msg)

time.sleep(20)