from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.implicitly_wait(10)

#1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;") #3000
# print(value)

#2. Scroll down till the element is visible
# flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value=driver.execute_script("return window.pageYOffset;")
# print(value)
#
# time.sleep(5)

#3. Scroll tll the end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(value)