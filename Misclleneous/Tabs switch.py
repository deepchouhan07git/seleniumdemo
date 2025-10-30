from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()

# reglink=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)

# New Tab =-- Opens a new tab and switches to the tab
# driver.get("https://demo.nopcommerce.com/")
# driver._switch_to.new_window('tab')
# driver.get("https://www.amazon.in/")

# New Window
driver.get("https://demo.nopcommerce.com/")
driver._switch_to.new_window('window')
driver.get("https://www.amazon.in/")
time.sleep(5)