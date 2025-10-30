from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(10)

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)

# Clicks on the button
act.context_click(button).perform()
# Click on the copy button
driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-copy']").click()

driver.switch_to.alert.accept()

time.sleep(5)
