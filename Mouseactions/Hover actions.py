from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


# Create ChromeOptions instance
serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Add explicit wait
wait = WebDriverWait(driver, 20)  # 20 seconds timeout
username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
username_input.send_keys("Admin")
pass_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
pass_input.send_keys("admin123")
wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))).click()


driver.implicitly_wait(20)
admin=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[1]//a[1]//span[1]")))
usrmgmt=wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space()='User Management']")))
users=driver.find_element(By.XPATH,"//a[normalize-space()='Users']")

act=ActionChains(driver)

act.move_to_element(admin).move_to_element(usrmgmt).move_to_element(users).click().perform()