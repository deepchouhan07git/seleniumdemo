from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame(0)

#mm/dd/yyyy
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/03/2025")

year="2026"
month="March"
date="15"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

# Select expected month and year
while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

# select date

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break;

