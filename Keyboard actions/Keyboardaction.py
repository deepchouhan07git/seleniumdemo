from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("Welcome")

act=ActionChains(driver)
# Select Control a
# act.key_down(keys.CONTROL)
# act.send_keys("a")
# act.key_up(keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Select control c
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Select TAB key
act.send_keys(Keys.TAB).perform()

# Select Control v
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)
