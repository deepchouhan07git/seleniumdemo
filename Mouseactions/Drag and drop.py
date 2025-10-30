from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
driver.implicitly_wait(10)

src_ele=driver.find_element(By.XPATH,"//div[@id='box3']")
trgt_ele=driver.find_element(By.XPATH,"//div[@id='box103']")

act=ActionChains(driver)
act.drag_and_drop(src_ele,trgt_ele).perform()

time.sleep(5)