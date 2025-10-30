from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
wait=WebDriverWait(driver,10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").click()

time.sleep(5)
# usrmgmt=wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space()='User Management']")))
# users=driver.find_element(By.XPATH,"//a[normalize-space()='Users']")

