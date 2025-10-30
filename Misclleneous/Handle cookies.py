from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Capture cookies from the site
cookies=driver.get_cookies()
print(len(cookies))

# Info about cookies
# for c in cookies:
#     #print(c)
#     print(c.get('name'),":",c.get('value'))

# Add new cookie to the browser
driver.add_cookie({"name":"Mycookie", "value":"12345"})
cookies=driver.get_cookies()
print(len(cookies))

# Delete specific cookie
driver.delete_cookie("Mycookie")
cookies=driver.get_cookies()
print(len(cookies))

# Delete all cookie
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))