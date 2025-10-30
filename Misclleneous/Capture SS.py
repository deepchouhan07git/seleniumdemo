from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\user\\PycharmProjects\\Selenium\\Misclleneous\\ss.png")
driver.save_screenshot(os.getcwd()+"\\ss.png")

driver.quit()