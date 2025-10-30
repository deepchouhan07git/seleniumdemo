from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Create ChromeOptions instance
serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Add explicit wait
wait = WebDriverWait(driver, 10)  # 10 seconds timeout
username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
username_input.send_keys("Admin")
pass_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
pass_input.send_keys("admin123")
wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))).click()


driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()
time.sleep(5)

rows=len(driver.find_elements(By.XPATH,"//div[@role='table']/div/div"))
print(rows)

count=0
for r in range(1,rows+1):
    stcd=driver.find_element(By.XPATH,"//div[@role='columnheader'][normalize-space()='']")
    if stcd.text=="Enabled":
        count=count+1
print(count)

